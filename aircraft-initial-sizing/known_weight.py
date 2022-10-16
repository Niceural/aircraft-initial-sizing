class KnowWeight:
    def __init__(self, config):
        payload = config["known weight"]["payload"]
        passenger = config["known weight"]["passenger"]
        crew = config["known weight"]["crew"]
        self.payload = PayloadWeight(payload["weight"], payload["safety factor"])
        self.passenger = PassengerWeight(passenger["number"], passenger["weight"], passenger["baggage weight"], passenger["safety factor"])
        self.crew = CrewWeight(crew["number"], crew["weight"], crew["safety factor"])

    def get_weight(self):
        return self.payload.get_weight() + self.passenger.get_weight() + self.crew.get_weight()

class PayloadWeight:
    def __init__(self, unfactored_weight, safety_factor):
        self.unfactored_weight = unfactored_weight # weight with no safety factor in kg
        self.safety_factor = safety_factor

    def get_weight(self):
        return self.unfactored_weight * self.safety_factor

class PassengerWeight:
    def __init__(self, number_of_passengers, passenger_weight, baggage_weight, safety_factor):
        self.number_of_passengers = number_of_passengers
        self.passenger_weight = passenger_weight
        self.baggage_weight = baggage_weight
        self.safety_factor = safety_factor

    def get_weight(self):
        return self.number_of_passengers * (self.passenger_weight + self.baggage_weight) * self.safety_factor

class CrewWeight:
    def __init__(self, number_of_crew, crew_weight, safety_factor):
        self.number_of_crew = number_of_crew
        self.crew_weight = crew_weight
        self.safety_factor = safety_factor

    def get_weight(self):
        return self.number_of_crew * self.crew_weight * self.safety_factor