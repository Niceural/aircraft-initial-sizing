class FuelWeight:
    def __init__(self, config):
        pass

    def get_fuel_weight_fraction(self, total_weight: float) -> float:
        return total_weight * pow(0.97 * 0.985 * 0.995, 4.)

class CruiseLeg:
    def __init__(self, param):
        self.name = param["name"]
        self.range = param["range"]
        self.altitude = param["altitude"]
        self.mach_number = param["mach number"]
        self.safety_factor = param["safety factor"]
