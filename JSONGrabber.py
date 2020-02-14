"""
Grabs useful info from info-[panoID].json for pano imgs
"""
import os, sys, json

JSON_FILE_FORMAT = "/info-%s.json"
# use absolute paths
PANO_DIR = "/Users/.../Desktop/smartIR/finished"
JSON_DIR = "/Users/.../Desktop/copleyPanos/infos"

def getIDs(dir): # obtain pano ids if json filename does not contain the pano id
    ids = []
    directory = os.fsencode(dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".png") and filename[:4] == "pano":
            ids.append(filename.split("-")[1])
    print(ids)
    return ids

def getIDs1(dir): # obtain pano ids if json filename contains pano id
    ids = []
    directory = os.fsencode(dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".json") and filename[:4] == "info":
            ids.append(filename.split("-")[1].split(".")[0])
    print(ids)
    return ids


def grabJSON(ids, dir): # use obtained ids to grab info from json and output
    result = []
    for id in ids:
        with open(dir+JSON_FILE_FORMAT%(id)) as json_file:
            print("Reading:%s"%(dir) + JSON_FILE_FORMAT%(id))
            data = json.load(json_file)
            d = {}
            d["id"] = id
            d["filename"] = "pano-%s-mx.png"%(id)
            d["calibration"] = 0.0
            d["neighborhood"] = "" #TODO: make neighborhood auto obtainable
            d["coord"] = {"lat": float(data["latitude"]), "lng": float(data["longitude"])}
            d["types"] = ["mx", "ir", "mymx"]
            result.append(d)
            print("Finished reading...")
    
    with open('./allPanoInfo.json', 'w') as outfile:
        json.dump(result, outfile)


if __name__ == "__main__":
    #info_dir = sys.argv[1]
    #source_dir = sys.argv[2]

    pano_ids = getIDs1(JSON_DIR)
    grabJSON(pano_ids, JSON_DIR)