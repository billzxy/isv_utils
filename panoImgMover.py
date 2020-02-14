"""
Moves (and renames) Pano images into designated directory
"""
import os, sys, shutil

IN_FILE_PREFIX = ""
OUT_FILE_FORMATS = ["pano-%s-mx.png", "pano-%s-ir.png", "pano-%s-mymx.png"]
# use absolute paths
SRC_DIR = "/Users/.../Desktop/copleyPanos/copleyOutput2/"
DST_DIR = "/Users/.../Desktop/isv/irstreetview/src/assets/pano-images/"

def getFilenames(src_dir):
    filenames = []
    suffixes = list(map(lambda f: '-'+f.split('-')[2] ,OUT_FILE_FORMATS))
    directory = os.fsencode(src_dir)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        for suffix in suffixes:
            if filename.endswith(suffix) and filename[:len(IN_FILE_PREFIX)] == IN_FILE_PREFIX:
                filenames.append(filename)
    filenames.sort()
    # print(filenames)
    return filenames


def moveFiles(filenames, src_dir, dst_dir): 
    for filename in filenames:
        pano_type = filename.split('-')[1].split('.')[0]
        src = src_dir+filename
        dst = dst_dir+pano_type+'/pano-'+filename
        shutil.move(src, dst)
        print(dst)
    

if __name__ == "__main__":
    #info_dir = sys.argv[1]
    #source_dir = sys.argv[2]

    filenames = getFilenames(SRC_DIR)
    moveFiles(filenames, SRC_DIR, DST_DIR)