#!/usr/bin/env python3

'''
Add permalinks (based on filename) to posts in folder (dirty way).
If it's already there, doesnt overwrite
'''

INPUT_FOLDER = ""
PERMALINK_BASE = ""

import os,sys


args = sys.argv[1:]

INPUT_FOLDER = args[0]
PERMALINK_BASE = args[1]

if "--help" in args:
	print (" Add permalinks (using filename) to posts (doesn't overwrite permalink if exists) ")
	print (" <script> INPUT_FOLDER PERMALINK ")
	print ("  ")
	print (" where permalink could be like /category/subfolder/, so the script ")
	print (" completes with the filename ")
	exit()


if not os.path.exists(INPUT_FOLDER):
	print (" folder doenst exist")
	exit()

if not PERMALINK_BASE.endswith("/"):
	PERMALINK_BASE += "/"

for root,subdir,files in os.walk(INPUT_FOLDER):
	for f in files:

		file_path = os.path.join(root,f)
		file_basename = os.path.splitext(os.path.basename(file_path))[0]

		print(" processing: " + file_path)

		file_contents = ""

		with open(file_path, 'r', encoding="utf-8") as tmp:
			file_contents = tmp.readlines()

		tmp = ""
		
		#we could use yaml but let's do it dirty ;D
		yaml_block = 0
		line_stop = 0
		has_permalink = False

		for i,line in enumerate(file_contents):
			if line.startswith("---"):
				if yaml_block == 0:
					yaml_block = 1
				else:
					line_stop = i
					break

			if line.startswith("permalink"):
				has_permalink = True 

		new_file = list()
		if has_permalink == False:
			new_file = file_contents[0:line_stop-2]
			new_file.append("permalink: " + PERMALINK_BASE + file_basename + "/\n")
			new_file += file_contents[line_stop-2:len(file_contents)]


			with open(file_path, 'w', encoding="utf-8") as tmp:
				tmp.writelines("".join(new_file))


print (" finished. Have a nice day.")