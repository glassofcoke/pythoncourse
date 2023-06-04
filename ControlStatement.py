
#IF-ELSE STATEMENT
"""
score = input("Please enter a score: ") #String INPUT
type(score) #Shows the data type
score = float(score) # Converts String to Float

if 100 >= score >= 60:
    print("A")
else:
    print("F")

#ELSE- IF STATEMENT

if 100 >= score >= 90:
    print("A")
elif 90 >= score >= 80:
    print("B")
elif 80 >= score >= 60:
    print("C")
elif 60 >= score >= 0:
    print("F")
else:
    print("Please enter a correct score: ")
"""

# LOOP STATEMENT

# WHILE
"""
i = 0
while i<9:
    i += 1
    print(i)
else:
    print("Loop ends right here")

i = 0
while i < 9:
    i+=1
    if i == 3:
        print("Skipped number")
        continue #skips the rest of the suite and goes back to testing
                 #if we use BREAK instead of continue, the loop finishes
    print(i)
else:
    print("Loop finished")
"""

# FOR STATEMENT

times = ["First", "Second", "Third"]

for i in times:
    print(i)
else:
    print("The loop ends")

# NESTED LOOP
for i in range(1,10):   #Outer Loop
    for j in range(1, i + 1):       #Inner Loop
        print("%dX%d=%-2d"%(j,i, j*i), end= " ") #String Formatting
    print()


