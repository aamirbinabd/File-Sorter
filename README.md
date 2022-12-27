# File Sorter
FileSorter is a simple Python script that helps you organize your files by moving them into separate folders based on their file formats. The script reads through the files in a given origin folder, extracts the file extensions, and moves each file into a folder with the same name as the file extension.

For example, all .pdf files will be moved into a folder called "pdf," all .docx files will be moved into a folder called "docx," and so on. If a folder for a particular file extension does not exist, the script will create it before moving the file.

To use the script, you will need to have Python 3 installed on your system. You can then run the script from the command line, specifying the path to the origin folder and the destination folder where you want the sorted files to be placed.

For example:

Copy code
python3 FileSorter.py /path/to/origin/folder /path/to/destination/folder
The script will then process all the files in the origin folder, creating the necessary folders in the destination folder and moving the files accordingly.

Note that the script will not create subfolders or otherwise sort the files beyond separating them by file extension. It is simply a tool for quickly organizing your files by type.

Tested on Ubuntu 20.04. 2 LTS

Suggestions and comments welcome ~ theaamir.com
