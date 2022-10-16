class EmptyWeight:
    def __init__(self, config):
        cfg = config["empty weight"]
        self.A: float = cfg["empty weight fraction - A"]
        self.C: float = cfg["empty weight fraction - C"]
        self.correction_factor: float = cfg["materials correction factor"]
        self.safety_factor: float = cfg["safety factor"]

    def get_empty_weight_fraction(self, total_weight: float) -> float:
        return self.A * pow(total_weight, self.C) * self.safety_factor
