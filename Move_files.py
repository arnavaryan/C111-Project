import os
import shutil

src="C:/Users/malho_9yypg6y/Downloads"
dest="C:/Users/malho_9yypg6y/Desktop/Document_Files"

list_of_files=os.listdir(src)
#print(list_of_files)

for file_name in list_of_files:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)