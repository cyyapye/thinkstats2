"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def pregnum_valid(resp):
    preg = nsfg.ReadFemPreg()
    pregmap = nsfg.MakePregMap(preg)
    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        if len(pregmap[caseid]) != pregnum:
            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = nsfg.ReadFemResp()
    
    assert(len(resp.pregnum) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(pregnum_valid(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
