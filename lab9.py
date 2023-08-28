#Lab 9
import os
#create directory if does not exist
if not os.path.exists("lab9"):
    os.mkdir("lab9")
#Write to file1.txt
with open("lab9/file1.txt","w") as file1:
    file1.write("VTU")
#Write to file2.txt
with open("lab9/file2.txt","w") as file2:
    file2.write("UNIVERSITY")
#Read from file1.txt and file2.txt and write to file3.txt
with open("lab9/file1.txt","r") as file1, open("lab9/file2.txt","r") as file2, open("lab9/file3.txt","w") as file3:
 content=file1.read()+file2.read()
 file3.write(content)