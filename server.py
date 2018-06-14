from flask import Flask, Response
from flask_cors import CORS
import requests, base64

app = Flask(__name__)
CORS(app)

def decode(encoded):
  return "".join(map(chr, base64.b64decode(encoded.replace("-", "/"))))

@app.route("/hasplayer/<username>")
def hasplayer(username):
  return "-" * (requests.get("https://hypixel.net/player/" + username).status_code == 200)

@app.route("/stats/<username>")
def stats(username):
  data = requests.get("https://plancke.io/hypixel/player/stats/%s#UHC" % username).text
  return data[data.find("UHC Champions") + 13:data.find("Warlords")]

@app.route("/proxy/<mimetype>/<url>")
def proxy(mimetype, url):
  return Response(requests.get(decode(url)).text, mimetype = decode(mimetype))

@app.route("/<pagename>")
def page(pagename):
  with open("public/" + pagename, "r", encoding = "utf-8") as f:
    return Response(f.read(), mimetype = "text/css" if pagename == "stylesheet.css" else "text/html")

@app.route("/")
def serveRoot():
  return Response(requests.get("https://c-6rtwjumjzx7877x24i6z0u8q9bufd8px2ehqtzikwtsyx2esjy.g00.gamepedia.com/g00/3_c-6rnsjhwfky.lfrjujinf.htr_/c-6RTWJUMJZX77x24myyux78x3ax2fx2fi6z0u8q9bufd8p.hqtzikwtsy.sjyx2frnsjhwfky_lfrjujinfx2f9x2f99x2fNsaXuwnyj.uslx3fajwx78ntsx3d6070301805060x26n65h.rfwpx3dstyMYRQ_$/$/$/$/$").text, mimetype = "image/png")

if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = 80, debug = True)