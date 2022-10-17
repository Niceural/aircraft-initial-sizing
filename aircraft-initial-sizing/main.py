import sys
import json

from empty_weight import EmptyWeight
from known_weight import KnowWeight

input_file_name = "./data/input.json"
file = open(input_file_name)
config = json.load(file)

known_weight = KnowWeight(config)
empty_weight = EmptyWeight(config)

W_0 = 33000.0
W_0 = known_weight / (1.0 - fuel_weight.get_weight_fraction(W_0) - empty_weight.get_weight_fraction(W_0))
