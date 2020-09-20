import os
import sys

verification = input("Am I in the correct folder? (Y/n)")

if (verification != "Y" or verification != " "):
    print("You should put me in the  folder you want me to modify")
    sys.exit()


all_files = os.listdir()

for item in all_files:
    fileName, fileType = item.split(".")
    
    if (fileType == "md"):
        day, month, year = fileName.split("-")
        os.system(f"mv {fileName}.md {year}-{month}-{day}.md")

print("Done!")