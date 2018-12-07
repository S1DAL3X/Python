import os

path = "R:/Games/dir1/"
os.chdir(str(path))
for root, dirs, files in os.walk(".", topdown = False):
  for name in files:
       print(name)
  for name in dirs:
      print(name)
