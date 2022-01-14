# Copyright (C) 2014-2022 Gleechi AB. All rights reserved.

## 
# @addtogroup Scripts 
# @{

## 
# @package check_header
# This module checks copyright headers of all source files in a directory.

import os
import sys
import argparse
    
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_INITIAL_DIR = os.path.join(CURRENT_DIR, "../../")
sys.path.append(os.path.join(CURRENT_DIR, "../../scripts"))

## Any filename that includes any of these will be excluded.
EXCLUDE_PATHS = ['cmake_generated', 'conan_build', '_resources.cpp', 'scripts\check\VirtualGraspSDK_']
## The header that we want in all source files.
HEADER = '// Copyright (C) 2014-2022 Gleechi AB. All rights reserved.'
## If TRUE, all source files will be overwritten; to be handled with care.
OVERWRITE = True

def receiveFilesFromDirectory(in_path, extensions, recursive = True, exclude_patterns = []):
    in_path = str(in_path)
    if in_path is None:
        if sys.version_info >= (3, 0):
            in_path = filedialog.askdirectory(initialdir=PATH_INITIAL_DIR)
        else:
            in_path = askdirectory(initialdir=PATH_INITIAL_DIR)

    if len(in_path) == 0:
        return [], in_path

    if recursive:
        files = [os.path.join(dp, f) for dp, dn, fn in os.walk(in_path) for f in fn]
    else:
        files = [os.path.join(in_path, f) for f in os.listdir(in_path)]

    files2 = []
    for file in files:
        excluded = False
        for exclude in exclude_patterns:
            if exclude in file:
                excluded = True
        if excluded:
             #print ("Skip excluded file", file)
            continue
        if not os.path.isfile(file):
		    #print ("Skip non-file", file)
            continue
        if extensions != "*" and file.lower().split('.')[-1] not in extensions:
            #print ("Skip not matching file", file)
            continue
        files2.append(os.path.normpath(file))

    return files2, os.path.join(in_path, in_path[in_path.rfind('/')+1:])

## Process the files by checking header lines and informing which headers are inconsistent.
def processFiles(filenames, old_, new_):
    for filename in filenames:
        # read content
        file = open(filename, 'r', encoding="utf-8")
        content = file.read()
        file.close()

        # check version with dots
        if old_ in content:
            print ("+ found", old_, "in", filename)
            if OVERWRITE:
                file = open(filename, 'w', encoding="utf-8")
                file.write(content.replace(old_, new_))
                file.close()
        #else:
        #    print ('- no', old_, 'found in', filename)  

        # check version with underscores
        old2 = '_sidebar_' + old_.replace('.','_')
        new2 = '_sidebar_' + new_.replace('.','_')        
        if old2 in content:
            print ("+ found", old2, "in", filename)
            if OVERWRITE:
                file = open(filename, 'w', encoding="utf-8")
                file.write(content.replace(old2, new2))
                file.close()
        #else:
        #    print ('- no', old2, 'found in', filename)            

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--old', required=True, help='Old version')
    parser.add_argument('--new', required=True, help='New version')
    args = parser.parse_args()

    filenames, path = receiveFilesFromDirectory(".", ['md'], True, EXCLUDE_PATHS)
    if len(filenames) == 0:
        print ("No files to process.")
        exit(-1)

    # process sequence of files
    processFiles(filenames, args.old, args.new)
else:
    print("check_header.py is being imported into another module")

## @} 
