import json, time, urllib.parse, subprocess
names = ["Roßbach, Braunsbedra","Bedra, Braunsbedra","Reichardtswerben","Tagewerben","Pettstädt, Weißenfels","Storkau, Weißenfels","Obschütz","Schortau","Leiha","Almsdorf, Mücheln","Mücheln (Geiseltal)","Branderoda","Zeuchfeld","Braunsbedra","Großkayna","Kleinkayna","Burgwerben","Markröhlitz","Janushügel","Uichteritz","Lunstädt","Gröst","Freyburg (Unstrut)","Weißenfels","Merseburg","Krumpa","Pörsten"]
out = {}
for n in names:
    q = urllib.parse.urlencode({"q": n + ", Sachsen-Anhalt", "format": "json", "limit": 1})
    try:
        r = json.loads(subprocess.run(["curl","-s","-A","rossbach-battle-map/0.1 (personal history project)","https://nominatim.openstreetmap.org/search?"+q],capture_output=True,text=True).stdout)
    except Exception as e:
        r = []; print("ERR", n, e)
    if r:
        out[n] = [float(r[0]["lat"]), float(r[0]["lon"]), r[0]["display_name"][:80]]
    print(n, out.get(n))
    time.sleep(1.1)
json.dump(out, open("data/places.json", "w"), indent=1, ensure_ascii=False)
