import sys
import os

# Ensure the server directory is in path so we can import util
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import util

def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    util.load_saved_artifacts()

def test_get_location_names():
    locations = util.get_location_names()
    assert isinstance(locations, list)
    assert "1st phase jp nagar" in locations

def test_get_estimated_price_known_location():
    price = util.get_estimated_price('1st phase jp nagar', 1000.0, 2, 2)
    assert isinstance(price, float)
    assert price > 0

def test_get_estimated_price_unknown_location():
    # An unknown location should default to the generic base logic
    price1 = util.get_estimated_price('Some Unknown Location XYZ', 1000.0, 2, 2)
    price2 = util.get_estimated_price('Another Unknown Location ABC', 1000.0, 2, 2)
    
    assert isinstance(price1, float)
    # The prices for unknown locations should match since they both hit loc_index = -1
    assert price1 == price2
