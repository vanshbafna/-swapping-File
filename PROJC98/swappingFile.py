# load file 1 into buffer
data = ""
with open("sample1.txt", "rb") as file:
    data = file.read()
# copy file 2 into file 1
with open("sample2.txt", "rb") as file1:
    with open("sample1.txt", "wb") as file2:
        file2.write(file1.read())
# save file 1 from buffer
with open("sample2.txt", "wb") as file:
    file.write(data)
print("Your file has been swapped successfully")
# clear memory
del data