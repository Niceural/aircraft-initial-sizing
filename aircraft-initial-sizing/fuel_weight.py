from math import *

class FuelWeight:
    def __init__(self, config):
        wf = config["mission segment weight fraction"]
        cruise_legs = config["cruise legs"]
        self.legs = []
        for i in range(len(cruise_legs)):
            self.legs.append(CruiseLeg(wf, cruise_legs[i]))

    def get_weight_fraction(self, l_over_d: float, tsfc: float) -> float:
        result = 0.
        for leg in self.legs:
            result += leg.get_weight_fraction(l_over_d, tsfc)
        result = 1. - result
        print(f"W_f/W_0 = {result}")
        return result


class CruiseLeg:
    def __init__(self, mission_segment_weight_fraction, cruise_leg):
        self.take_off_fraction: float = mission_segment_weight_fraction["take off"]
        self.climb_fraction: float = mission_segment_weight_fraction["climb"]
        self.landing_fraction: float = mission_segment_weight_fraction["landing"]
        self.range: float = cruise_leg["range (km)"]
        self.altitude: float = cruise_leg["altitude (ft)"]
        self.velocity: float = cruise_leg["velocity (mach)"]
        self.safety_factor: float = cruise_leg["safety factor"]

    def get_weight_fraction(self, l_over_d: float, tsfc: float) -> float:
        velocity_m_s = self.velocity * 309.67 # hardcoded value for speed of sound at 25,000 ft
        result = 3 - self.take_off_fraction - self.climb_fraction - self.landing_fraction
        result += exp(- self.range * tsfc / velocity_m_s / l_over_d)
        return result * (1. + self.safety_factor)
