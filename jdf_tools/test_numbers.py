#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
    @license: MIT, see COPYING for details.
"""
from numbers import numbers

def test_numbers():
    n = numbers()
    assert n.convNumber2letter(2014) == "DEUX MILLE QUATORZE "
    assert n.convNumber2letter(37000) == "TRENTE SEPT MILLE "


if __name__ == '__main__':
    n = numbers()
    print n.convNumber2letter(2014)
    print n.convNumber2letter(37000)

