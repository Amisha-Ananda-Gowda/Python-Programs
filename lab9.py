import os
if not os.path.exists("lab9"):
    os.mkdir("lab9")
with open("lab9/file1.txt","w") as file1:
    file1.write("VTU")
with open("lab9/file2.txt","w") as file2:
    file2.write("UNIVERSITY")
with open("lab9/file1.txt","r") as file1, open("lab9/file2.txt","r") as file2, open("lab9/file3.txt","w") as file3:
    content=file1.read()+file2.read()
    file3.write(content)