"""
Unit test for lvm_read.py
"""

import numpy as np
from lvm_read import read

def test_short_lvm():
    data = read('../data/short.lvm', read_from_pickle=False)
    np.testing.assert_equal(data[0]['data'][0,0],0.914018)

    data = read('../data/short.lvm', read_from_pickle=True)
    np.testing.assert_equal(data[0]['data'][0, 0], 0.914018)


def test_with_empty_fields_lvm():
    data = read('../data/with_empty_fields.lvm', read_from_pickle=False)
    np.testing.assert_equal(data[0]['data'][0,7],-0.011923)

if __name__ == '__mains__':
    np.testing.run_module_suite()