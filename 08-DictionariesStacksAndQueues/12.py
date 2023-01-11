book= {
    "title": "Hobbit",
    "author": "J.R.R. Tołkien",
    "release": 1937,
    "is lit": True,
    "contains": ['fights','orcs','dragon','treasure']
}
import json
file= open('favourite.json',"w",encoding='UTF-8')
json.dump(book, file,ensure_ascii=False)
file.close()