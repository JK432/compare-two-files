# Write a program to compare two files 
f1=open("file1.txt","r")
f2=open("file2.txt","r")

if(f1.read()==f2.read()):
  print("same")
else:
  print("notsame")
  