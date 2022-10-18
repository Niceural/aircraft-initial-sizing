class EmptyWeight:
    def __init__(self, config):
        cfg = config["empty weight"]
        self.A: float = cfg["empty weight fraction - A"]
        self.C: float = cfg["empty weight fraction - C"]
        self.materials_correction_factor: float = cfg["materials correction factor"]
        self.safety_factor: float = cfg["safety factor"]

    def get_weight_fraction(self, total_weight: float) -> float:
        result = self.A * pow(total_weight, self.C) * (1. + self.safety_factor) * self.materials_correction_factor
        print(f"W_e/W_0 = {result}")
        return result
