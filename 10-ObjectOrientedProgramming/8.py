class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no= 1
    def turn_on(self):  
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            print(f"TV is on, channel {self.channel_no}")
        else:
            print("TV is off")
    def set_channel(self, new_no):
        self.channel_no=new_no

lg= TV()

lg.show_status()
lg.turn_on()
lg.show_status()
lg.turn_off()
lg.turn_on()
lg.set_channel(5)
lg.show_status()