#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self, maximum_speed, measure):
        """ Car constructor. """
        self.maximum_speed = maximum_speed
        self.measure = measure

    def __str__(self):
        return 'Car with the maximum speed of {0} {1}'.format(
            self.maximum_speed,
            self.measure,
        )


class Boat:
    def __init__(self, maximum_speed):
        """Boat constructor"""
        self.maximum_speed = maximum_speed

    def __str__(self):
        return 'Boat with the maximum speed of {0} knots'.format(
            self.maximum_speed,
        )


car = Car(120, 'mph')
boat = Boat(250)

print(car)
print(boat)
