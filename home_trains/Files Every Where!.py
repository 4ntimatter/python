import glob

list_of_files = glob.glob('./files/*.txt')
for f in list_of_files:
    print(f)