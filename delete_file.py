print("----------------------------------------------")
# --------------------- delete file ---------------------
# -------------------------------------------------------

# import os

# path = "test6.txt"

# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("File not found.")

# -------------------------------------------------------
import os
import shutil

path = "empty_folder"

try:
    # os.remove(path) # delete a file
    # os.rmdir(path) # delete an empty directory
    shutil.rmtree(path)  # delete a directory containing files
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("You do not have permission to delete that folder.")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path, "was deleted")
