class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no= 1
        self.channel_list=[]
        self.volume=0
    def turn_on(self):  
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def show_status(self):
        if self.is_on:
            if self.channel_no>len(self.channel_list):
                print(f"TV is on, channel {self.channel_no}\nVolume:{self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no} ({self.channel_list[self.channel_no-1]})")
        else:
            print("TV is off")
    def set_channel(self, new_no):
            self.channel_no=new_no
    def set_channels(self,channels_list):
        self.channel_list= channels_list
    def show_channels(self):
        if self.channel_list==[]:
                print("No channels were programmed. Try to program any channel.")
        else: 
            print("List of avaiable channels:")
            for x in range(len(self.channel_list)):
                print(f"{x+1}. ",f"{self.channel_list[x]}") 
    def volume_inc(self):
        if self.volume<=10:
            self.volume+=1
            if self.volume==11:
                self.volume=10
    def volume_dcr(self):
        if self.volume>=0:
            self.volume-=1
            if self.volume==(-1):
                self.volume=0
        

lg= TV()
#lg.show_status()
#print()
lg.turn_on()
#print()
#lg.show_status()
#print()
#lg.turn_off()
#print()
#lg.turn_on()
#print()
#lg.set_channel(5)
#print()
#lg.show_status()
#print()
#lg.show_channels()
#print()
lg.set_channels(["TVP1","TVP2","Polsat","TVN","Filmbox","Discovery"])
print()
#lg.show_channels()
#print()
#lg.show_status()
#print()
#lg.set_channel(1)
#lg.show_status()
#print()
#lg.set_channel(2)
#lg.show_status()
#print()
#lg.set_channel(3)
#lg.show_status()
#print()
#lg.set_channel(4)
#lg.show_status()
#print()
#g.set_channel(5)
#lg.show_status()
#print()
#lg.set_channel(6)
#lg.show_status()
#print()
lg.set_channel(7)
lg.show_status()
print()
i=0
while i<15:
    lg.volume_inc()
    i+=1
lg.show_status()