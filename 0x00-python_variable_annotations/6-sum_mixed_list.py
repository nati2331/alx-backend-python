#!/usr/bin/env python3
'''Task 6
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the sum of int and floats.
    '''
    return float(sum(mxd_lst))
