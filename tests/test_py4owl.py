#!/usr/bin/env python
"""Tests for `py4owl` package."""
# pylint: disable=redefined-outer-name
from py4owl import __version__
from py4owl.py4owl_interface import GreeterInterface
from py4owl.py4owl_impl import HelloWorld

def test_version():
    """Sample pytest test function."""
    assert __version__ == "0.0.1"

def test_GreeterInterface():
    """ testing the formal interface (GreeterInterface)
    """
    assert issubclass(HelloWorld, GreeterInterface)

def test_HelloWorld():
    """ Testing HelloWorld class
    """
    hw = HelloWorld()
    name = 'yvain'
    assert hw.greet_the_world(name) == f"Hello world, {name} !"

