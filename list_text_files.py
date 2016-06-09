import glob

filelist = glob.glob('*.txt')
for filename in filelist:
    print(filename)