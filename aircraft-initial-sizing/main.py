import sys
import json

from empty_weight import EmptyWeight
from known_weight import KnowWeight

input_file_name = "./data/input.json"
file = open(input_file_name)
config = json.load(file)

known_weight = KnowWeight(config)
empty_weight = EmptyWeight(config)
# fuel_weight = null
