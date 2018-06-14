import urllib.request, base64

while True:
  url = input("Enter URL (talk to parents about permission form for music trip thing) >>> ")
  try:
    print("data:image/png;base64," + base64.b64encode(urllib.request.urlopen(url).read()).decode("utf-8"))
  except:
    raise