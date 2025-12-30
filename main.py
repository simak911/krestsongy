pocet = 189

data = {}

for i in range (1, pocet+1):
    nazev = f"./Sets/PLAYLIST ({i})"
    f = open(nazev, "r", encoding="utf-8")
    lines = f.readlines()
    dateline = lines[1]
    songlines = []
    for i in range (2, len(lines)):
        line = lines[i]
        if "type=\"song\"" in line:
            songlines.append(line)
    
    # zjistime datum
    parts = dateline.split("\"")
    date = parts[1]
    print(date)

    # zjistime nazev pisne
    for songline in songlines:
        parts2 = songline.split("\"")
        if len(parts2) > 1:
            sn = parts2[1]

            if sn in data.keys():
                data[sn].append(date)
            else:
                data[sn] = [date]

f = open("./output.csv", "w", encoding="utf-8")
for key in data.keys():
    s = key + ";"
    i = 0
    for date in data[key]:
        s += date + ";"
        i += 1
    ss = str(i) + ";" + s + "\n"
    f.write(ss)
f.close()
    
