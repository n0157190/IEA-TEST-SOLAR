#!/usr/bin/env python3

import solar

def test_get_observer_location():
    val = get_observer_location()
    assert val == '39.0438 -77.4874'
