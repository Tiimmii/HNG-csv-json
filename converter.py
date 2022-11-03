import json
import csv
import hashlib

#Reading the NFT.csv file
with open ("NFT Naming csv - All Teams.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        row[6] = []
        for rows in row[6]:
            row[6].append({"hair":rows[0], "eyes":rows[1], "teeth":rows[2], "clothing":rows[3], "accessories":rows[4], "expression":rows[5], "strength":rows[6], "weakness":rows[7]})
        data.append({"TEAM NAMES":row[0],"SerialNumber":row[1], "FileName":row[2], "Name":row[3], "Description":row[4], "Gender":row[5], "Attributes":row[6], "UUID":row[7]})
        # attributes = row["Attributes"]
        # attributes = []
        # for row in attributes:
        #     attributes.append({"hair":row[0], "eyes":row[1], "teeth":row[2], "clothing":row[3], "accessories":row[4], "expression":row[5], "strength":row[6], "weakness":row[7]})

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

    