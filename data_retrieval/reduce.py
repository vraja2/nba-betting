import glob
import json
import os

outfile = "all_boxscores.json"

files_names = glob.glob(os.path.join('data', "*.json"))
all_data = {}
for f in files_names:
	with open(f) as infile:
		print os.path.basename(f)
		all_data[os.path.basename(f)] = json.load(infile)

with open(outfile, 'w') as outfile:
	json.dump(all_data, outfile)