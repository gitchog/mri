# units.py

"""
Module for unit conversion functions and SI constants for the MRI probe project.
"""

# SI Constants

MASS = {
    'gram': 1e-3,
    'kilogram': 1,
    'ton': 1e3,
}

LENGTH = {
    'millimeter': 1e-3,
    'centimeter': 1e-2,
    'meter': 1,
    'kilometer': 1e3,
}

TIME = {
    'second': 1,
    'minute': 60,
    'hour': 3600,
}

# Unit conversion functions

def convert_mass(value, from_unit, to_unit):
    """Convert mass from one unit to another."""
    return value * (MASS[from_unit] / MASS[to_unit])


def convert_length(value, from_unit, to_unit):
    """Convert length from one unit to another."""
    return value * (LENGTH[from_unit] / LENGTH[to_unit])


def convert_time(value, from_unit, to_unit):
    """Convert time from one unit to another."""
    return value * (TIME[from_unit] / TIME[to_unit])
