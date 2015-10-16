#!/usr/bin/env python3

'''
Find if all tags have their own index page.
Runs on current working dir; uses [TAG_FOLDER]/[tag]/index.html and _posts folder
'''

TAG_FOLDER = "tag"
POST_FOLDER = "_posts"

TPL_TAG_INDEX='''---
title: {tag}
---
'''


import os,sys

INPUT_FOLDER = os.getcwd()


args = sys.argv[1:]

if "--help" in args:
	print (" Find if all tags have their own index page. Runs on current working dir. ")
	print (" uses /<TAG_FOLDER>/<tag>/index.html and /_posts/ for posts")
	exit()


TAG_FOLDER  = os.path.join(INPUT_FOLDER, TAG_FOLDER)
POST_FOLDER = os.path.join(INPUT_FOLDER, POST_FOLDER)

# list the tags with indexes

#tags_with_indexes = next(os.walk(TAG_FOLDER))[1]
tags_with_indexes = list()
# this searches the direct subfolders of a folder 
#(from: http://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory/973488#973488)

# we must check if it has an index.html
for i in next(os.walk(TAG_FOLDER))[1]:
	if os.path.exists(os.path.join(TAG_FOLDER,i,"index.html")):
		tags_with_indexes.append(i)

print (" \n the current tags with indexes: " + ",".join(tags_with_indexes))
print ("")

tags_posts = list()
# now go through the files and list the tags

for root,subdir,files in os.walk(POST_FOLDER):
	for f in files:
		if f.startswith("_"):
			continue

		file_path = os.path.join(root,f)
		file_basename = os.path.splitext(os.path.basename(file_path))[0]

		print(" processing: " + file_basename)

		file_contents = ""

		with open(file_path, 'r', encoding="utf-8") as tmp:
			file_contents = tmp.readlines()

		tmp = ""
		
		#we could use yaml but let's do it dirty ;D
		yaml_block = False
		
		for i,line in enumerate(file_contents):
			if line.startswith("---"):
				if yaml_block == False:
					yaml_block = True
				else:
					break

			if line.startswith("tags"):
				tmp = line.split("[")[1].split("]")[0].split(",")
				tmp_item = ""
				for item in tmp:
					if not item: 
						continue
					tmp_item = item.strip()
					if not tmp_item in tags_with_indexes and not tmp_item in tags_posts:
						tags_posts.append(tmp_item)

#inform the results
print("------------------------------------------------\n")
if len(tags_posts) == 0:
	print (" Everything is OK. You rock!.")
	exit()

print (" There are tags without indexes. These are: ")
print ( ",".join(tags_posts))

answer = input(" do you want to create the indexes for those? ")
if answer.lower() in ("n", "no", "effit", "meh"):
	print (" Ok, as you please. Have a nice day")
	exit()

tmp = ""
tmp_folder = ""

for item in tags_posts:
	tmp_folder = os.path.join(TAG_FOLDER, item)
	proper_title = item.replace("-", " ")

	print ("\n :: creating index for: " + proper_title )
	proper_tag = input("    proper title? leave empty to keep it as is ")

	if not proper_tag:
		proper_title = item
	else:
		proper_title = proper_tag

	try:
		os.makedirs(tmp_folder)
	except OSError:
		print("      folder for {} and can't be created. Exiting".format(item))
		exit()

	with open(os.path.join(tmp_folder,"index.html"), 'w', encoding="utf-8") as tmp:
		tmp.writelines(TPL_TAG_INDEX.format(tag=proper_title))


print ("\n done! ")