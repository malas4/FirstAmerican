import json

data = """{
    "Buyer": ["Hatch John D"
            ],
    "DocumentType": "Deed",
    "Position": null,
    "Vesting":null,
    "Borrowers": "",
    "ChildSeqIDs":[]
}"""

# parse the data

json_dict = json.loads(data)
with open ("FileA.json", "w") as outfile:
    json.dump(json_dict, outfile)

data_B= {
    "AssessRecord": {
      "ID": "123-111",
      "Latitude":"33.9183",
      "Addresses":[],
      "Owners":[
        "HATCH TEST TRUST",
        "HATCH JOHN D",
        "HATCH SALLY"]
    }
}
json_dictb = json.dumps(data_B)

with open("FileB.json", "w") as outfile:
    outfile.write(json_dictb)

data_schema = """{
    "Buyer": [1
            ],
    "DocumentType": "Deed",
    "Position": null,
    "Vesting":null,
    "Borrowers": "",
    "ChildSeqIDs":[]
}"""
json_data_schema= json.loads(data_schema)
with open("FileC.json", "w") as outfile:
    json.dump(json_data_schema, outfile)


data_schemaA = """{
    "Buyer": ["John Maxwell D" 
            ],
    "DocumentType": "Deed",
    "Position": null,
    "Vesting":null,
    "Borrowers": "",
    "ChildSeqIDs":[]
}"""
json_data_schemaA= json.loads(data_schemaA)
with open("FileD.json", "w") as outfile:
    json.dump(json_data_schemaA, outfile)
