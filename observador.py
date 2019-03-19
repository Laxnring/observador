import sys, requests
import re
from urllib.parse import unquote

#Host: api.observador.pt
#GET /wp/lists/featured HTTP/1.1
#GET /wp/items/id/3047882 HTTP/1.1

req = requests.get("https://api.observador.pt/wp/lists/featured")
r = req.json()

keys = ["id", "title", "fullTitle", "lead", "text"]
articles = []
structure = dict()
#print(len(r))
for i in range(0, len(r)):
    structure = dict()
    structure.fromkeys(keys, None)
    structure["id"] =  req.json()[i]["id"]
    structure["title"] =  req.json()[i]["title"]
    structure["fullTitle"] =  req.json()[i]["fullTitle"]
    structure["lead"] =  req.json()[i]["lead"]
    articles.append(structure)

#for i in range(0, len(articles)):
text_req = requests.get("https://api.observador.pt//wp/items/id/" + str(articles[0]["id"]))
body = text_req.json()["body"]
#body =  re.sub(r'<.+?>', '', body)
#body = unquote(body)
#body = body.replace("&#8220;", "'")
#body = body.replace("&#8221;", "'")
#body = body.replace("&#8216;", "'")
#body = body.replace("&#8217;", "'")
#body = body.replace("&#8230;", "'")
#body = body.replace("&#8217;", "'")
#body = body.replace("&nbsp;", " ")

# REMOVER ENTRE HTTPS E /
#body = re.sub(r"http\S+", "", body)
#print(body)
for i in range(0, len(articles)):
    text_req = requests.get("https://api.observador.pt//wp/items/id/" + str(articles[i]["id"]))
    body = text_req.json()["body"]

    with open(str(articles[i]["id"]) + ".html", "w+", encoding="utf-8") as text_file:
        text_file.write("<h1>" + articles[i]["title"] + "</h1>")
        text_file.write("<h2>" + articles[i]["fullTitle"] + "</h2>")
        text_file.write(body)

with open("index.html", "w+", encoding="utf-8") as text_file:
    for i in range(0, len(articles)):
        text_file.write("<head><meta charset='UTF-8'></head><body><a href='" + str(articles[i]["id"]) +".html" + "'>" + articles[i]["title"] + "</a>" + "\n" + "<br></body>")