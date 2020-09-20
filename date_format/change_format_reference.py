import os
import sys

standard = ["DD", "MM", "YYYY"]

def main():
    if len(sys.argv) > 3:
        search_path   = sys.argv[1] 
        new_format    = sys.argv[2] 
        delimeter     = sys.argv[3]
    else:
        search_path   = input("Enter directory path to search : ")
        # new_format = input("Put the new Date format: (DD-MM-YYYY) ")
        delimeter = input("Put the delimiter:")


    # new_format = new_format.split(delimiter)
    # new_format = [standard.index(i) for i in new_format]

    os.chdir(search_path)
    all_files = os.listdir() 


    for item in all_files:
        fileName, fileType = item.split(".")
        
        if (fileType == "md"):
            day, month, year = fileName.split(delimeter)
            os.system(f"mv {fileName}.md {year}-{month}-{day}.md")

    print("Done!")

if __name__ == "__main__":
    main()