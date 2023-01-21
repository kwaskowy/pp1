class Thermometer():
    def __init__(self):
        self.is_on=False
        self.temperature= 0.0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def measurement(self):
        import random
        if self.is_on:
            self.temperature=round(random.uniform(34.0,42.0),1)
        else: 
            print("Turn the thermometer on first.")
            self.temperature=0.0
    def display(self):
        if self.is_on:
            if self.temperature==0.0:
                print("---,measure temperature first")
            elif 34<=self.temperature<35:
                print(f"Temperature: {self.temperature}C (hypothermia)")
                self.temperature= 0.0
            elif 35<=self.temperature<=37:
                print(f"Temperature: {self.temperature}C (normal)")
                self.temperature= 0.0
            elif 37<self.temperature<41:
                print(f"Temperature: {self.temperature}C (fever)")
                self.temperature= 0.0
            elif 41<=self.temperature<=42.0:
                print(f"Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)")
                self.temperature= 0.0
        else: print("Turn the thermometer on first.")
