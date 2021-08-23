"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
from operator import itemgetter

import first
from numpy import append
import thinkstats2


def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    if len(hist) == 0:
        return 0
    
    m = hist[0]
    mfreq = hist.Freq(m)
    for x in hist:
        freq = hist.Freq(x)
        if freq > mfreq:
            mfreq = freq
            m = x
    return m


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    modes = []
    for x in hist:
        freq = hist.Freq(x)
        modes.append((x, freq))
    modes = sorted(modes, key=lambda x: x[1], reverse=True)
    return modes


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert mode == 39, mode

    # test AllModes
    modes = AllModes(hist)
    assert modes[0][1] == 4693, modes[0][1]

    for value, freq in modes[:5]:
        print(value, freq)

    print('%s: All tests passed.' % script)

    firstwgtmn, otherwgtmn = firsts.totalwgt_lb.mean(), others.totalwgt_lb.mean()
    print(f'firsts mean: {firstwgtmn}, others mean: {otherwgtmn}')

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print(f'cohen effect size: {d}')


if __name__ == '__main__':
    main(*sys.argv)
