print("----------------------------------------------")
# --------------------- copy file ---------------------
# -----------------------------------------------------
# copyfile():   copies contents of a file
# copy():       copyfile() + permission mode + destination can be a directory
# copy2():      copy() + copies metadata (file's creation and modification times)

import shutil

with open("test3.txt", "w") as file:
    file.write("Yooooooo\nThis is some text\nSee ya!")

shutil.copyfile("test3.txt", "copytest3.txt")  # (source, destination)
