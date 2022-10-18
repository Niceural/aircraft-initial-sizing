import sys
import json
from empty_weight import EmptyWeight
from known_weight import KnownWeight
from fuel_weight import FuelWeight

input_file_name = "./data/input.json"
file = open(input_file_name)
config = json.load(file)

known_weight = KnownWeight(config)
empty_weight = EmptyWeight(config)
fuel_weight = FuelWeight(config)

l_over_d = config["wing"]["L/D max"] * config["wing"]["L/D cruise factor"]
tsfc = config["engine"]["tsfc cruise"] * 2.

W_0 = 33000.0
for i in range(10):
    W_0 = known_weight.get_weight() / (1.0 - fuel_weight.get_weight_fraction(l_over_d, tsfc) - empty_weight.get_weight_fraction(W_0))
    print(f"Iteration {i+1}: {W_0} kg")