import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


# make a duplicate of an existing file
if path.exists("textfile.txt"):
  # get the path to the file in the current directory
  src = path.realpath("textfile.txt");

  # # let's make a backup copy by appending "bak" to the name
  dst = src + ".bak"
  # # now use the shell to make a copy of the file
  shutil.copy(src,dst)

  # # copy over the permissions, modification times, and other info
  shutil.copystat(src, dst)

  # # rename the original file
  os.rename("textfile.txt", "newfile.txt")

  # now put things into a ZIP archive
  root_dir,tail = path.split(src)
  shutil.make_archive("archive", "zip", root_dir)  #will zip all the files of the directory

  # more fine-grained control over ZIP files for putting specific files in zip
  with ZipFile("testzip.zip","w") as newzip:
    newzip.write("newfile.txt")
    newzip.write("textfile.txt.bak")
