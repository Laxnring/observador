import sys, requests
import re
from urllib.parse import unquote

req = requests.get("https://api.observador.pt/wp/lists/featured")
r = req.json()

keys = ["id", "title", "fullTitle", "lead", "text"]
articles = []
structure = dict()
for i in range(0, len(r)):
    structure = dict()
    structure.fromkeys(keys, None)
    structure["id"] =  req.json()[i]["id"]
    structure["title"] =  req.json()[i]["title"]
    structure["fullTitle"] =  req.json()[i]["fullTitle"]
    structure["lead"] =  req.json()[i]["lead"]
    articles.append(structure)

text_req = requests.get("https://api.observador.pt//wp/items/id/" + str(articles[0]["id"]))
body = text_req.json()["body"]

for i in range(0, len(articles)):
    text_req = requests.get("https://api.observador.pt//wp/items/id/" + str(articles[i]["id"]))
    body = text_req.json()["body"]

    with open(str(articles[i]["id"]) + ".html", "w", encoding="utf-8") as text_file:
        text_file.write("<meta charset='UTF-8'><link rel='stylesheet' id='wp-block-library-css' href='https://observador.pt/wp-includes/css/dist/block-library/style.min.css?ver=9db0bf24a320f03534dc189e081dbc6566fd0f72' type='text/css' media='all' /><link rel='stylesheet' id='observador-style-css' href='https://observador.pt/wp-content/themes/observador/assets/build/css/observador.min.css?ver=9db0bf24a320f03534dc189e081dbc6566fd0f72' type='text/css' media='all' /><style>p {font-size:150%;margin-right:10%;margin-left:10%} h1 {margin-right:10%;margin-left:10%} h2 {margin-right:10%;margin-left:10%} img{width:50%;display:block;margin:auto;} div {font-size:100%;margin-right:10%;margin-left:10%} </style>")
        text_file.write("<h1>" + articles[i]["title"] + "</h1>")
        text_file.write("<h2>" + articles[i]["fullTitle"] + "</h2>")
        text_file.write(body)

with open("index.html", "w", encoding="utf-8") as text_file:
    text_file.write("""        
        <head><meta charset='UTF-8'><link rel='stylesheet' id='wp-block-library-css'  
        href='https://observador.pt/wp-includes/css/dist/block-library/style.min.css?ver=9db0bf24a320f03534dc189e081dbc6566fd0f72' 
        type='text/css' media='all' />
        <link rel='stylesheet' id='observador-style-css' 
        href='https://observador.pt/wp-content/themes/observador/assets/build/css/observador.min.css?ver=9db0bf24a320f03534dc189e081dbc6566fd0f72'
        type='text/css' media='all' />
        <style>body {font-size:100%;text-align:center;} </style>
        </head>
        <body>
        <h1>O Observador Pirata</h1>""")
    for i in range(0, len(articles)):
        text_file.write("<a href='" + str(articles[i]["id"]) +".html" + "'>" + articles[i]["title"] + "</a>" + "\n" + "<br>")

# Incorporar FLASK e passar para o raspberry pi.
