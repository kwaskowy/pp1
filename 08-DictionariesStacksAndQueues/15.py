ICAO={
    "A":"Alfa",
    "B":"Bravo",
    "C":"Charlie",
    "D":"Delta",
    "E":"Echo",
    "F":"Foxtrot",
    "G":"Golf",
    "H":"Hotel",
    "I":"India",
    "J":"Juliett",
    "K":"Kilo",
    "L":"Lima",
    "M":"Mike",
    "N":"November",
    "O":"Oscar",
    "P":"Papa",
    "Q":"Quebec",
    "R":"Romeo",
    "S":"Sierra",
    "T":"Tango",
    "U":"Uniform",
    "V":"Victor",
    "W":"Whiskey",
    "X":"X-ray",
    "Y":"Yankee",
    "Z":"Zulu",
}
file= open("ICAO.txt","w")
for k,v in ICAO.items():
    if k=="Z":
        file.write(k)
        file.write(": ")
        file.write(v)
    else:
        file.write(k)
        file.write(": ")
        file.write(v)
        file.write("\n")
file.close()
