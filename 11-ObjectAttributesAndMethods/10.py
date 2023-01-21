class Phones():
    phon_id= 0
    def __init__(self,brand,model,price):
        self.is_on=False
        self.photos_taken= 0
        self.brand= brand
        self.model= model
        self.price= price
        Phones.phon_id+=1
        self.id= Phones.phon_id
    def __str__(self):
        if self.is_on:
            return f"Phone no.{self.id}:\nBrand: {self.brand}\nModel: {self.model}\nPrice: {self.price}zł\nPhotos taken: {self.photos_taken}"
        else: return f"Phone no.{self.id}:\nBrand: {self.brand}\nModel: {self.model}\nPrice: {self.price}zł\nPhotos taken: turn on phone first."
    def toggle_power(self):
        if self.is_on:
            self.is_on=False
        else: self.is_on=True
    def take_photo(self):
        self.photos_taken+=1
        print("*SNAP*\nphoto has been taken")
    
ip= Phones("Apple","iPhone 13","4268")
xmi= Phones("Xiaomi","mi12","3799")
print(ip)
print()
print(xmi)
print()
print()
ip.toggle_power()
for x in range(15):
    ip.take_photo()
print(ip)
print()
print(xmi)
        