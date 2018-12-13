"""
Functions for dealing with mass and volume of helium/air
mixtures and calculating lifting force.

Any function that begins with "get_" assumes units and returns
specific units. "get_" functions convert units based on the
constants defined at the top of this module.
"""

import math

# constants
DENSITY_AIR = 1.225 #kg/m^3 at STP
DENSITY_HELIUM = 0.179 #kg/m^3 at STP
FEET_PER_METER = 3.28084
ACC_GRAVITY = 9.8066 #m/s^2


def volume(diameter):
    """
    return the volume of a sphere, given the diameter
    """
    return 4/3*math.pi*(diameter/2)**3


def mass(density, volume):
    """
    return the mass as a function of density and volume
    units not assumed
    """
    return density*volume


def diameter(volume):
    """
    return the diameter of a sphere of given volume
    """
    
    return 2*(((3*volume)/(4*math.pi))**(1/3))


def get_mass_air(volume):
    """
    return the mass (g) of a volume (ft^3) of air
    """
    volume = volume/FEET_PER_METER**3 # ft^3 -> m^3
    m = mass(DENSITY_AIR, volume) # DENSITY_AIR~kg/m^3
    m = m * 1000 # kg to g
    return m


def get_mass_helium(volume):
    """
    return the mass (g) of a volume (ft^3) of helium
    """

    return volume * 5.05



def get_bouyant_force_helium(volume):
    """
    return the mass (g) that can be lifted by a
    volume (ft^3) of helium. NOT ACTUALLY A FORCE

    https://en.wikipedia.org/wiki/Lifting_gas#Hydrogen_versus_helium
    """
    volume = volume/FEET_PER_METER**3 # ft^3 -> m^3
    force = (DENSITY_AIR - DENSITY_HELIUM) * volume * ACC_GRAVITY # kg/m^3
    force = force * 1000 # kg -> g
    grams = force * volume
    return grams



def get_helium_ratio(diameter, mass):
    """
    return the ratio of helium to air required to make
    a baloon of arbitrary diameter (in) and mass (g)
    float statically. The ratio is of volumes, so
    a value of .6 means the baloon at a given diameter
    and mass should be 60% helium and 40% air by volume.
    """
    diameter = diameter/12 # in -> ft
    v_total = volume(diameter) # ft^3

    # approximate the volume of helium required
    v_helium = 0
    m_helium = get_bouyant_force_helium(v_helium)
    while m_helium < mass:
        v_helium += 0.001
        m_helium = get_bouyant_force_helium(v_helium)

    print(m, v_helium, v_total)
    pass
