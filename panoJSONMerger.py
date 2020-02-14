"""
Merge newly added pano info into existing pano info
"""
import os, sys, json
from jsonmerge import merge, Merger

IN_JSON_0_PATH = "/Users/.../Desktop/isv/irstreetview/mock/data/panos.json"
IN_JSON_1_PATH = "/Users/.../Desktop/copleyPanos/copleyOutput2/allPanoInfo.json"
OUT_JSON_PATH =  IN_JSON_0_PATH

schema = {        
    "mergeStrategy": "append"
}

json0 = ''
with open(IN_JSON_0_PATH) as json_file_0:
    print("Reading: "+IN_JSON_0_PATH.split('/')[-1] )
    json0 = json.load(json_file_0)
    print("Length: ",len(json0))

json1 = ''
with open(IN_JSON_1_PATH) as json_file_1:
    print("Reading: "+IN_JSON_1_PATH.split('/')[-1] )
    json1 = json.load(json_file_1)
    print("Length: ",len(json1))

print("Merging...")
merger = Merger(schema)
result = merger.merge(json0, json1)
print("Output length: ",len(result))

with open(OUT_JSON_PATH, 'w') as outfile:
    json.dump(result, outfile)
    print("Saved merged JSON into "+OUT_JSON_PATH.split('/')[-1])

