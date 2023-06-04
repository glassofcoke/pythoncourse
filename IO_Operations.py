"""
#Open text.txt. If not exist, python will create the file
f = open("text.txt",'w',encoding = 'utf8')

inputs = input("Input: ")
f.write(inputs)
f.close()

f = open("text.txt", 'r')
print(f.read(20))
print(f.read())
f.close()

f = open("text.txt", 'a')
f.write(" I Append more content. This is just an exercise")
f.close()

f = open("text.txt",'r')
print(f.read())
f.close()
"""
#Use WITH statement to open file
with open("text1.txt",'w') as f:
    f.write("Python is cool \nThis is a test \nI like big fat titties")
#Use WITH statement to read file
with open("text1.txt",'r') as f:
    print(f.read())

#open file
with open("text1.txt", "r") as f:
    line = f.readline()
    print("Read one line: %s" % (line))

    lines = f.readlines()
    print(lines)

