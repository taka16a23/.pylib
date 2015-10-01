#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $Id: builder.py 105 2014-02-22 09:25:25Z t1 $
# $Revision: 105 $
# $Date: 2014-02-22 18:25:25 +0900 (Sat, 22 Feb 2014) $
# $Author: t1 $
# $LastChangedBy: t1 $
# $LastChangedDate: 2014-02-22 18:25:25 +0900 (Sat, 22 Feb 2014) $

r"""builder -- DESCRIPTION

"""

import sys as _sys
import os as _os
import abc

# for debug
import cgitb as _cgitb
_cgitb.enable(format='text')


__revision__ = '$Revision: 105 $'
__version__ = '0.1.0'


#==============================================================================
class Vehicle(object):

    def __init__(self, type_name):
        self.type = type_name
        self.wheels = None
        self.doors = None
        self.seats = None

    def view(self):
        print(
            "This vehicle is a " +
            self.type +
            " with; " +
            str(self.wheels) +
            " wheels, " +
            str(self.doors) +
            " doors, and " +
            str(self.seats) +
            " seats."
            )

#==============================================================================
class VehicleBuilder(object):
    """
    An abstract builder class, for concrete builders to be derived from.
    """
    __metadata__ = abc.ABCMeta

    @abc.abstractmethod
    def make_wheels(self):
        raise

    @abc.abstractmethod
    def make_doors(self):
        raise

    @abc.abstractmethod
    def make_seats(self):
        raise

#==============================================================================
class CarBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("Car ")

    def make_wheels(self):
        self.vehicle.wheels = 4

    def make_doors(self):
        self.vehicle.doors = 3

    def make_seats(self):
        self.vehicle.seats = 5

#==============================================================================
class BikeBuilder(VehicleBuilder):

    def __init__(self):
        self.vehicle = Vehicle("Bike")

    def make_wheels(self):
        self.vehicle.wheels = 2

    def make_doors(self):
        self.vehicle.doors = 0

    def make_seats(self):
        self.vehicle.seats = 2

#==============================================================================
class VehicleManufacturer(object):
    """
    The director class, this will keep a concrete builder.
    """

    def __init__(self):
        self.builder = None

    def create(self):
        """
        Creates and returns a Vehicle using self.builder
        Precondition: not self.builder is None
        """
        assert not self.builder is None, "No defined builder"
        self.builder.make_wheels()
        self.builder.make_doors()
        self.builder.make_seats()
        return self.builder.vehicle


#==============================================================================
if (__name__ == "__main__"):
    manufacturer = VehicleManufacturer()

    manufacturer.builder = CarBuilder()
    car = manufacturer.create()
    car.view()

    manufacturer.builder = BikeBuilder()
    bike = manufacturer.create()
    bike.view()


# This vehicle is a Car  with; 4 wheels, 3 doors, and 5 seats.
# This vehicle is a Bike with; 2 wheels, 0 doors, and 2 seats.

def _test():
    r"""Test function."""
    return _os.EX_OK

if __name__ == '__main__':
    _sys.exit(_test())



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# builder.py ends here
