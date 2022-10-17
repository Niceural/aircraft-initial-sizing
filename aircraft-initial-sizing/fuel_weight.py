from math import *

class FuelWeight:
    def __init__(self, config):
        pass

    def get_weight_fraction(self, total_weight: float) -> float:
        return total_weight * pow(0.97 * 0.985 * 0.995, 4.)

class CruiseLeg:
    def __init__(self, fuel_fractions, leg):
        self.take_off_fraction: float = fuel_fractions["take off"]
        self.climb_fraction: float = fuel_fractions["climb"]
        self.landing_fraction: float = fuel_fractions["landing"]
        self.range: float = leg["range"]
        self.altitude: float = leg["altitude"]
        self.mach: float = leg["mach number"]
        self.safety_factor: float = leg["safety factor"]

    def get_weight_fraction(self, total_weight, l_over_d, C):
        result = total_weight * self.take_off_fraction * self.climb_fraction * self.landing_fraction
        result = result * (- self.range * C) / (exp())
        return result
