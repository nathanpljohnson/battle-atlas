import json, subprocess, time, urllib.parse
# historical name -> modern search string
Q = {
 "Telnitz": "Telnice, Brno-venkov", "Sokolnitz": "Sokolnice", "Sokolnitz castle": "zámek Sokolnice", "Kobelnitz": "Kobylnice, Brno-venkov",
 "Puntowitz": "Ponětovice", "Schlappanitz": "Šlapanice", "Girzikowitz": "Jiříkovice", "Pratzen": "Prace, Brno-venkov",
 "Blasowitz": "Blažovice", "Krug": "Kruh, Jiříkovice", "Holubitz": "Holubice, Vyškov", "Bosenitz": "Podolí, Brno-venkov",
 "Santon": "Santon, Tvarožná", "Welatitz": "Velatice", "Posoritz post": "Stará pošta, Kovalovice", "Kowalowitz": "Kovalovice",
 "Krzenowitz": "Křenovice, Vyškov", "Raussnitz": "Rousínov", "Austerlitz": "Slavkov u Brna", "Hostieradek": "Hostěrádky-Rešov",
 "Aujezd": "Újezd u Brna", "Satschan": "Žatčany", "Menitz": "Měnín", "Raigern": "Rajhrad", "Zuran": "Žuráň",
 "Pratzeberg": "Mohyla míru, Prace", "Stare Vinohrady": "Staré vinohrady, Blažovice", "Bellowitz": "Bedřichovice", "Turas": "Tuřany, Brno",
 "Latein": "Slatina, Brno", "Walspitz": "Hodějice", "Tvarozna": "Tvarožná", "Zbysov": "Zbýšov, Vyškov",
}
out = {}
for k, q in Q.items():
    url = "https://nominatim.openstreetmap.org/search?" + urllib.parse.urlencode({"q": q + ", Czechia", "format": "json", "limit": 1})
    r = json.loads(subprocess.run(["curl", "-s", "-A", "BattleAtlas/0.1 (personal history project)", url], capture_output=True, text=True).stdout or "[]")
    if r: out[k] = [round(float(r[0]["lat"]), 5), round(float(r[0]["lon"]), 5)]
    print(k, out.get(k), (r[0]["display_name"][:60] if r else "NOT FOUND"))
    time.sleep(1.1)
json.dump(out, open("places_raw.json", "w"), ensure_ascii=False, indent=1)
