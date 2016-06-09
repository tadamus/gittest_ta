
# these are my changes TA
# Usage: python list_text_files.py
import glob

filelist = glob.glob('*.txt')
for filename in filelist:
    print(filename)
