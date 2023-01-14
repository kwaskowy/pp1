class music():
    def __init__(self,artist,track_title,album,year):
        self.artist= artist
        self.track= track_title
        self.album= album
        self.year= year
    def __str__(self):
        return f"Artist: {self.artist}\nTrack: {self.track}\nAlbum: {self.album}\nYear: {self.year}"

shape= music("Ed Sheeran","Hearts Don't Break Around Here","Divide","2017")
print(shape)
