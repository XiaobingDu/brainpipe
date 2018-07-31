"""Functional connectivity."""
import logging

import numpy as np
from scipy import stats, signal

from ..info_th.mi import _mi
from ..sys import set_log_level


logger = logging.getLogger('brainpipe')


def _fc_corr(x, y, **kwargs):
    """Pearson correlation between two time-series."""
    return stats.pearsonr(x, y)


def _fc_mtd(x, y, **kwargs):
    """Multiplication of temporal derivatives between two time-series."""
    ts = np.diff(np.r_[x, x[-1]]) * np.diff(np.r_[y, y[-1]])
    ts /= np.std(ts)
    return ts, np.ones((len(ts),), dtype=float)


def _fc_cmi(x, y, **kwargs):
    """Cross mutual information."""
    return _mi(x, y), 1.


def _fc_mtd_mean(x, y, **kwargs):
    """Multiplication of temporal derivatives between two time-series."""
    _ts, _pval = _fc_mtd(x, y, **kwargs)
    return _ts.mean(), _pval.mean()


def _axes_correction(axis, ndim, num):
    """Get a slice at a specific axis."""
    axes = [slice(None)] * ndim
    axes[axis] = num
    return axes


def _directional_ts(ts_1, ts_2, axis, lag):
    """Add a jitter to a time-series."""
    assert ts_1.shape == ts_2.shape
    assert isinstance(lag, int) and (lag >= 0)
    # Truncate time-series :
    n_pts = ts_1.shape[axis]
    ax_1 = _axes_correction(axis, ts_1.ndim, slice(0, n_pts - lag))
    ax_2 = _axes_correction(axis, ts_2.ndim, slice(lag, n_pts))
    ts_1_lag, ts_2_lag = ts_1[ax_1], ts_2[ax_2]
    assert ts_2_lag.shape == ts_2_lag.shape
    return ts_1_lag, ts_2_lag

###############################################################################
#                        STATIC FUNCTIONAL CONNECTIVITY
###############################################################################


def _sfc(ts, meth, **kwargs):
    n_pts = int(len(ts) / 2)
    ts_1, ts_2 = ts[0:n_pts], ts[n_pts::]
    return meth(ts_1, ts_2, **kwargs)


def sfc(ts_1, ts_2, axis=0, measure='corr', bins=64, mtd_mean=True,
        verbose=None):
    """Compute static functional connectivity (sFC).

    Parameters
    ----------
    ts_1, ts_2 : array_like
        Array of time series with the same shape.
    axis : int | 0
        Location of the time dimension.
    measure : {'corr', 'mtd', 'cmi'}
        Name of the connectivity measure. Use either 'corr' (pearson
        correlation), 'mtd' (multiplication of temporal derivatives) or 'cmi'
        (cross-mutual information)
    bins : int | 64
        Number of bins. See `brainpipe.info_th.cmi` for further details.
    mtd_mean : bool | True
        The MTD method is time-resolved. Hence use True if you only want to get
        the mean of the MTD or False fo the time-resolved version of it.
    verbose : bool, str, int, or None
        The verbosity of messages to print. If a str, it can be either
        PROFILER, DEBUG, INFO, WARNING, ERROR, or CRITICAL.

    Returns
    -------
    ts_sfc : array_like
        Array of static connectivity.
    p_values : array_like
        Array of p-values. Only available if the selected method is 'corr'
        otherwise it returns 1.

    Notes
    -----
    J.M Shine, Estimation of dynamic functional connectivity using
    Multiplication of Temporal Derivatives, 2015
    Schreiber, Measuring information transfer, 2000
    """
    assert all([isinstance(k, np.ndarray) for k in (ts_1, ts_2)])
    assert ts_1.shape == ts_2.shape
    assert axis < ts_1.ndim
    assert measure in ['corr', 'mtd', 'cmi']
    set_log_level(verbose)
    # Get fc measure :
    _mtd_meth = {False: _fc_mtd, True: _fc_mtd_mean}[mtd_mean]
    meth = {'corr': _fc_corr, 'mtd': _mtd_meth, 'cmi': _fc_cmi}[measure]
    # Concatenate ts_1 and ts_2 :
    ts = np.concatenate((ts_1, ts_2), axis=axis)
    # Apply sfc :
    logger.info("Compute sFC using %s" % measure)
    args = np.apply_along_axis(_sfc, axis, ts, meth, bins=bins)
    # Return the sfc and p-values :
    ts_ax = _axes_correction(axis, args.ndim, 0)
    pv_ax = _axes_correction(axis, args.ndim, 1)
    return args[ts_ax], args[pv_ax]


def directional_sfc(ts_1, ts_2, lag, axis=0, measure='corr', bins=64,
                    mtd_mean=True, verbose=None):
    """Compute directional static functional connectivity using a time lag.

    This is equivalent to the `brainpipe.connectivity.sfc` function except that
    sfc is computed between x[t] and y[t - lag].

    Parameters
    ----------
    ts_1, ts_2 : array_like
        Array of time series with the same shape.
    lag : int
        Time lag in sampes to apply to `ts_2`. Must be an integer > 0.
    axis : int | 0
        Location of the time dimension.
    measure : {'corr', 'mtd', 'cmi'}
        Name of the connectivity measure. Use either 'corr' (pearson
        correlation), 'mtd' (multiplication of temporal derivatives) or 'cmi'
        (cross-mutual information)
    bins : int | 64
        Number of bins. See `brainpipe.info_th.cmi` for further details.
    mtd_mean : bool | True
        The MTD method is time-resolved. Hence use True if you only want to get
        the mean of the MTD or False fo the time-resolved version of it.
    verbose : bool, str, int, or None
        The verbosity of messages to print. If a str, it can be either
        PROFILER, DEBUG, INFO, WARNING, ERROR, or CRITICAL.

    Returns
    -------
    ts_sfc : array_like
        Array of static connectivity.
    p_values : array_like
        Array of p-values. Only available if the selected method is 'corr'
        otherwise it returns 1.

    Notes
    -----
    J.M Shine, Estimation of dynamic functional connectivity using
    Multiplication of Temporal Derivatives, 2015
    Schreiber, Measuring information transfer, 2000
    """
    set_log_level(verbose)
    # Add jitter to a time-series :
    ts_1_lag, ts_2_lag = _directional_ts(ts_1, ts_2, axis, int(lag))
    # Compute sfc :
    logger.info("Compute directional sFC using %s" % measure)
    return sfc(ts_1_lag, ts_2_lag, axis, measure, bins, mtd_mean)


###############################################################################
#                        DYNAMIC FUNCTIONAL CONNECTIVITY
###############################################################################

def _dfc(ts, meth, sp_idx, win_opt, **kwargs):
    # Split ts_1 and ts_2 :
    n_pts = int(len(ts) / 2)
    ts_1, ts_2 = ts[0:n_pts], ts[n_pts::]
    # Predefine sliding window array :
    ts_win = np.zeros((2, sp_idx.shape[0]), dtype=ts.dtype)
    for k, (start, stop) in enumerate(sp_idx):
        # Window correction :
        win_1 = win_opt * ts_1[start:stop]
        win_2 = win_opt * ts_2[start:stop]
        ts_win[:, k] = meth(win_1, win_2, **kwargs)
    return ts_win[0, :], ts_win[1, :]


def dfc(ts_1, ts_2, win, axis=0, sf=1., measure='corr', overlap=None,
        win_opt=None, bins=64, verbose=None):
    """Compute dynamic functional connectivity (dFC).

    The only difference with sFC is that dFC used a sliding window with an
    overlap.

    Parameters
    ----------
    ts_1, ts_2 : array_like
        Array of time series with the same shape.
    win : int, float
        Window size. If `win` is a float, it's considered in seconds and the
        sampling frequency is then used to make the conversion in samples.
    axis : int | 0
        Location of the time dimension.
    sf : float | 1.
        Sampling frequency. Only used if `win` is a float.
    measure : {'corr', 'mtd', 'cmi'}
        Name of the connectivity measure. Use either 'corr' (pearson
        correlation), 'mtd' (multiplication of temporal derivatives) or 'cmi'
        (cross-mutual information)
    overlap : float | None
        Overlap percent between successive windows. It should be a float
        and 0. <= overlap < 1. with 0. (or None) for no overlap between windows
    win_opt : {None, 'hamming', 'hanning'}
        Window optimization parameter if a sliding window is used.
    bins : int | 64
        Number of bins. See `brainpipe.info_th.cmi` for further details.
    verbose : bool, str, int, or None
        The verbosity of messages to print. If a str, it can be either
        PROFILER, DEBUG, INFO, WARNING, ERROR, or CRITICAL.

    Returns
    -------
    ts_sfc : array_like
        Array of dynamic connectivity.
    p_values : array_like
        Array of p-values. Only available if the selected method is 'corr'
        otherwise it returns 1.
    time : array_like
        The resulting time vector.

    Notes
    -----
    J.M Shine, Estimation of dynamic functional connectivity using
    Multiplication of Temporal Derivatives, 2015
    Schreiber, Measuring information transfer, 2000
    """
    set_log_level(verbose)
    assert all([isinstance(k, np.ndarray) for k in [ts_1, ts_2]])
    assert isinstance(sf, (int, float)) and isinstance(axis, int)
    assert ts_1.shape == ts_2.shape
    assert isinstance(win, (int, float)) and (win > 0)
    n_pts = ts_1.shape[axis]
    time = np.arange(n_pts) / sf

    # Checkout win size and overlap :
    overlap = 0. if not isinstance(overlap, (int, float)) else overlap
    assert 0. <= overlap < 1.
    win = int(win * sf) if isinstance(win, float) else win
    step = win - int(overlap * win)
    # Get split index for moving average :
    start = np.arange(0, n_pts - win, step).astype(int)
    stop = np.arange(win, n_pts, step).astype(int)
    assert len(start) == len(stop)
    sp_idx = np.c_[start, stop]
    # Get window opimization ;
    if win_opt is 'hamming':
        w_opt, w_msg = signal.hamming(win), 'hamming'
    elif win_opt is 'hanning':
        w_opt, w_msg = signal.hanning(win), 'hanning'
    else:
        w_opt, w_msg = np.ones((win,), dtype=float), 'None'
    # Split time :
    time_sp = np.array([time[k:i].mean() for (k, i) in sp_idx])

    # Get fc measure :
    logger.info("Compute dFC using %s" % measure)
    logger.info('    Sliding window = %i; step=%i samples' % (win, step))
    logger.info('    Window optimization : %s' % w_msg)
    meth = {'corr': _fc_corr, 'mtd': _fc_mtd_mean, 'cmi': _fc_cmi}[measure]
    # Concatenate time-series :
    ts = np.concatenate((ts_1, ts_2), axis)
    # Compute dFC :
    args = np.apply_along_axis(_dfc, axis, ts, meth, sp_idx, w_opt, bins=bins)
    # Return the sfc and p-values :
    ts_ax = _axes_correction(axis, args.ndim, 0)
    pv_ax = _axes_correction(axis, args.ndim, 1)
    return args[ts_ax], args[pv_ax], time_sp


def directional_dfc(ts_1, ts_2, win, lag, axis=0, sf=1., measure='corr',
                    overlap=None, win_opt=None, bins=64, verbose=None):
    """Compute directional dynamic functional connectivity (dFC).

    This is equivalent to the `brainpipe.connectivity.sfc` function except that
    sfc is computed between x[t] and y[t - lag].

    Parameters
    ----------
    ts_1, ts_2 : array_like
        Array of time series with the same shape.
    win : int, float
        Window size. If `win` is a float, it's considered in seconds and the
        sampling frequency is then used to make the conversion in samples.
    lag : int
        Time lag in sampes to apply to `ts_2`. Must be an integer > 0.
    axis : int | 0
        Location of the time dimension.
    sf : float | 1.
        Sampling frequency. Only used if `win` is a float.
    measure : {'corr', 'mtd', 'cmi'}
        Name of the connectivity measure. Use either 'corr' (pearson
        correlation), 'mtd' (multiplication of temporal derivatives) or 'cmi'
        (cross-mutual information)
    overlap : float | None
        Overlap percent between successive windows. It should be a float
        and 0. <= overlap < 1. with 0. (or None) for no overlap between windows
    win_opt : {None, 'hamming', 'hanning'}
        Window optimization parameter if a sliding window is used.
    bins : int | 64
        Number of bins. See `brainpipe.info_th.cmi` for further details.
    verbose : bool, str, int, or None
        The verbosity of messages to print. If a str, it can be either
        PROFILER, DEBUG, INFO, WARNING, ERROR, or CRITICAL.

    Returns
    -------
    ts_sfc : array_like
        Array of dynamic connectivity.
    p_values : array_like
        Array of p-values. Only available if the selected method is 'corr'
        otherwise it returns 1.
    time : array_like
        The resulting time vector.

    Notes
    -----
    J.M Shine, Estimation of dynamic functional connectivity using
    Multiplication of Temporal Derivatives, 2015
    Schreiber, Measuring information transfer, 2000
    """
    set_log_level(verbose)
    # Add jitter to a time-series :
    ts_1_lag, ts_2_lag = _directional_ts(ts_1, ts_2, axis, int(lag))
    # Compute dfc :
    logger.info("Compute directional dFC using %s" % measure)
    return dfc(ts_1_lag, ts_2_lag, win, axis, sf, measure, overlap, win_opt,
               bins, verbose)


###############################################################################
#                                  SUMMARY
###############################################################################


def fc_summarize(ts, axis=0, method='std', verbose=None):
    """Summarize dFC measure across the time dimension.

    Parameters
    ----------
    ts : array_like
        Connectivity array to summarize.
    axis : int | 0
        Location of the time dimension.
    method : {'std', 'coefvar', 'mean'}
        Method used to summarize connectivity arrays across the time dimension.
        Use 'std' for standard deviation, 'mean' or 'coefvar' (see notes)

    Notes
    -----
    Javier Gonzalez-Castillo, The spatial structure of resting state
    connectivity stability on the scale of minutes, 2014
    """
    set_log_level(verbose)
    assert isinstance(ts, np.ndarray)
    assert isinstance(axis, int) and (axis <= ts.ndim)
    assert method in ['std', 'coefvar', 'mean']
    # Summarize :
    if method == 'std':
        logger.info("Summarize using the standard deviation")
        return ts.std(axis=axis)
    elif method == 'mean':
        logger.info("Summarize using the mean")
        return ts.mean(axis=axis)
    elif method == 'coefvar':
        logger.info("Summarize using the coefficient of variation")
        # Correlation -> Fisher's z-score :
        ts_zs = np.arctanh(ts)
        # Summarized :
        ts_m = np.mean(ts_zs, axis=axis)
        ts_m[ts_m == 0.] = 1.
        ts_sum = np.std(ts_zs, axis=axis) / ts_m
        # Fisher's z-score -> Correlation :
        return np.tanh(ts_sum)