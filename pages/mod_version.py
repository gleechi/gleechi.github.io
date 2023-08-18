# Copyright (C) 2014-2022 Gleechi AB. All rights reserved.

## 
# @addtogroup Scripts 
# @{

## 
# @package check_header
# This module checks copyright headers of all source files in a directory.

# TODOS:
# - automatic, proper handling of sidebar, topnav, release notes

import os
import sys
import re
import argparse
import shutil

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_INITIAL_DIR = os.path.join(CURRENT_DIR, "../../")
sys.path.append(os.path.join(CURRENT_DIR, "../../scripts"))

## Any filename that includes any of these will be excluded.
EXCLUDE_PATHS = ['cmake_generated', 'conan_build', '_resources.cpp', 'scripts\check\VirtualGraspSDK_']
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

def replaceWildcards(string, pattern, replacementPattern):
    splitPattern = re.split(r'([*?])', pattern)
    splitReplacement = re.split(r'([*?])', replacementPattern)
    if (len(splitPattern) != len(splitReplacement)):
        raise ValueError("Provided pattern wildcards do not match")
    reg = ""
    sub = ""
    for idx, (regexPiece, replacementPiece) in enumerate(zip(splitPattern, splitReplacement)):
        if regexPiece in ["*", "?"]:
            if replacementPiece != regexPiece:
                raise ValueError("Provided pattern wildcards do not match")
            reg += f"(\\S{regexPiece if regexPiece == '*' else ''})" # Match anything but whitespace
            sub += f"\\{idx + 1}" # Regex matches start at 1, not 0
        else:
            reg += f"({re.escape(regexPiece)})"
            sub += f"{replacementPiece}"
    return re.sub(reg, sub, string)

def replaceVersion(filenames, old_, new_):
    for filename in filenames:
        # read content
        file = open(filename, 'r', encoding="utf-8")
        content = file.read()
        file.close()

        # check version with dots        
        if old_ in content:
            print ("+ found", old_, "in", filename)
            content = content.replace(old_, new_)
            if OVERWRITE:
                file = open(filename, 'w', encoding="utf-8")                
                file.write(content)
                file.close()
        #else:
        #    print ('- no', old_, 'found in', filename)  

        # check version with underscores
        old2 = '_sidebar_' + old_.replace('.','_')
        new2 = '_sidebar_' + new_.replace('.','_')        
        if old2 in content:
            print ("+ found", old2, "in", filename)
            content = content.replace(old2, new2)
            if OVERWRITE:
                file = open(filename, 'w', encoding="utf-8")
                file.write(content)
                file.close()
        #else:
        #    print ('- no', old2, 'found in', filename)  

        '''
        # add version
        old2 = 'sidebar: main_sidebar_' + old_.replace('.','_')
        if old2 in content:
            print ("+ found", old2, "in", filename)
            content = content.replace(old2, old2 + '\nversion: ' + new_)
            if OVERWRITE:
                file = open(filename, 'w', encoding="utf-8")
                file.write(content)
                file.close()
        '''
        
        '''
        content =  "the [grasp studio](unity_component_vggraspstudio.html) scene."
        print("before:" + content)
        content = replaceWildcards(content, "](*.html", "](*.{{page.version}}.html")
        print("after:" + content)
        '''
        
        '''
        # mod links
        content = replaceWildcards(content, "](*.html", "](*." + new_ + ".html")
        if OVERWRITE:
            file = open(filename, 'w', encoding="utf-8")
            file.write(content)
            file.close()
        '''

def adjustReleaseNotes(filename, old_, new_):
    file = open(filename, 'r', encoding="utf-8")
    content = file.read()
    file.close()

    file = open(filename, 'w', encoding="utf-8")
    content = content.replace("V" + new_ + " (", "V" + old_ + "(")
    file.write(content) 
    file.close()

def adjustTopNav(filename, old_, new_):
    file = open(filename, 'r', encoding="utf-8")
    content = file.read()
    file.close()

    file = open(filename, 'w', encoding="utf-8")
    idx = content.find("        - title: Unity SDK " + old_)
    out = content[:idx] + "        - title: Unity SDK " + new_ + "\n          url: /index." + new_ + ".html\n" + content[idx:]
    file.write(out) 
    file.close()     

if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--old', required=True, help='Old version')
    parser.add_argument('--new', required=True, help='New version')
    args = parser.parse_args()

    if not os.path.isdir(args.new):
        print ()
        answer = input("There is no folder " + args.new + ". Do you want to create it [Y/n]?") 
        if answer == "Y" or answer == "y" or answer == "":
            shutil.copytree(args.old, args.new)
        else:
            exit(-1)

    # Create sidebar for new version
    content = open("../_data/sidebars/main_sidebar_" + args.old.replace('.', '_') + ".yml", 'r', encoding="utf-8").read()
    sidebar = "../_data/sidebars/main_sidebar_" + args.new.replace('.', '_') + ".yml"
    open(sidebar, 'w', encoding="utf-8").write(content)

    # Gather .md files and process sequence of files
    filenames, path = receiveFilesFromDirectory(args.new, ['md'], True, EXCLUDE_PATHS)    
    replaceVersion(filenames, args.old, args.new)
    
    # Replace the "last" version in the sidebar that is checked to show if there's an update.
    replaceVersion([sidebar, "../_includes/sidebar.html"], args.old, args.new)

    # Add a new version entry to the topnav menu
    adjustTopNav("../_data/topnav.yml", args.old, args.new)

    # Re-adjust the release notes (version was replaced above in this .md file as well)
    #adjustReleaseNotes(args.new + "/unity/release_notes.md", args.old, args.new)

else:
    print("check_header.py is being imported into another module")

## @} 
