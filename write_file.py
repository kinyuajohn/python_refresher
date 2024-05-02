print("----------------------------------------------")
# --------------------- write/append file ---------------------
# -------------------------------------------------------------

# text = "Yoooooooooo!\nThis is some text.\nHave a good one!\n"
# text2 = "************\nOverwrites content\n"
# text3 = "************\nAppend more information"

text = "Text 1\n"
text2 = "Text 2\n"
text3 = "Text 3"

# write to a file (overwrites previous content)
with open("test2.txt", "w") as file:
    file.write(text)

# read
with open("test2.txt", "r") as file:
    print(file.read())

# write to a file (overwrites previous content)
with open("test2.txt", "w") as file:
    file.write(text2)

# read
with open("test2.txt", "r") as file:
    print(file.read())

# append to a file (overwrites previous content)
with open("test2.txt", "a") as file:
    file.write(text3)

# read
with open("test2.txt", "r") as file:
    print(file.read())
