import os

#get the current process id
print("process ID: ", os.getpid())

#get the process ID (PID) of the calling process.
print("Parent process ID: ", os.getppid())

#get the current directory
cwd = os.getcwd()
print("Current directory: ", cwd)

#Changes the current directory
os.chdir("C:/")
print("New directory: ", os.getcwd())

#Get a list containing the names of the entries in the directory given by path
print("All the files: ", os.listdir(cwd))

#creating a variable to check the directory
a = os.getcwd()
print(a)
#changing it back to the right directory
os.chdir("C:/Users/aglas/Documents/PyCharm Workspace/Python Huawei Course")

#Checking the new directory
b = os.getcwd()
print(b)

#print all the file names under the current directory(including files in subdirectories)
for root, dirs, files in os.walk(cwd):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))


#Get the absolute pathname
print("Absolute pathname: ",os.path.abspath("text.txt"))

#Returns true or false if the path exists
print("Exists or not?!: ", os.path.exists("text1.txt"))

#Returns the size of path
print("Size: ", os.path.getsize("text.txt"))

#Determines if path is a file
print("Is file: ", os.path.isfile("text.txt"))

#Determines if the path is a folder
print("Is it a folder?: ", os.path.isdir("text.txt"))
