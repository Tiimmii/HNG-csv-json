import json
import csv
import hashlib

#Reading the NFT.csv file
with open ("NFT Naming csv - All Teams.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    list = []
    for row in reader:
        split = row[6].split(";")
        for items in split:
            item = items.split(":")
        data.append({"format":"CHIP-0007","name":row[2],"description":row[4], "minting_tool":row[0], "sensitive_content":False, "series_number":row[1], "series_total":420, "gender":row[5], "Attributes":item, "UUID":row[7]})
#Converting the NFT.csv file to JSON
with open ("NFT Naming.json", "w") as f:
    json.dump(data, f, indent=3)

#Hashing and appending each JSON data in the JSON data file 
with open ("NFT Naming.json") as f:
    datas = json.load(f)
    for data in datas:
        data_2 = f"{data}"
        hashed = hashlib.sha256(data_2.encode()).hexdigest()
        data.update({"Hash":hashed})
    datas.append({"Hash":hashed})

#Dumping the Hashed JSON data to a new JSON file
with open ("Hashed NFT Naming.json", "w") as f:
    json.dump(datas, f, indent=3)

#Reading the Hashed JSON data file
with open("Hashed NFT Naming.json", "r") as f:
    name = json.load(f)

#Convertung the Hashed JSON data file back to csv format (filename.output.csv)
with open ("NFT Naming csv - All Teams.output.csv", "w", newline="") as f:
    fieldnames = name[0].keys()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for names in name:
        writer.writerow(names)

    