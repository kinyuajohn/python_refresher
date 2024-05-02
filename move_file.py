print("----------------------------------------------")
# --------------------- move file ---------------------
# -----------------------------------------------------

import os

# source = "test4.txt"
# destination = "C:/Users/ADMN/Desktop/test4.txt"

# try:
#     if os.path.exists(destination):
#         print("There is already a file there.")
#     else:
#         os.replace(source, destination)
#         print(source, "was moved")
# except FileNotFoundError:
#     print(source, "not found.")

# -----------------------------------------------------
source = "test_folder"
destination = "C:/Users/ADMN/Desktop/test_folder"

try:
    if os.path.exists(destination):
        print("There is already a folder there.")
    else:
        os.replace(source, destination)
        print(source, "was moved")
except FileNotFoundError:
    print(source, "not found.")
