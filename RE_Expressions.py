import re       #Import re module

print(re.match('www','www.huawei.com').span())  #match from the start of the text
print(re.match('com','www.huawei.com')) #cannot match from the middle of the text

#If we want to look for a match anywhere in the text
#print(re.match('com','www.huaewi.com').span())

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are smarter than (.*)', line)
if searchObj:
    print("searchObj.group(): ", searchObj.group())
    print("searchObj.group(1): ",searchObj.group(1))
    print("searchObj.group(2): ",searchObj.group(2))
else:
    print("Nothing found!")

pattern = re.compile(r'\d+')
n = pattern.match('one12twothree34four')
print(n)

m = pattern.search('one12twothree34four')
print(m)
print(m.group())

phone = '2020-0101-000 # this is a phone number'
#remove the number sign(#) and everything after it
num = re.sub(r'#.*',"", phone)
print("phone number: ", num)
#remove everything that isn't a digit
num = re.sub(r'\D',"", phone)
print("phone number: ",num)

#find all the numbers in the text
text = "tomorrow is 12/04/2023. Today is 11/04/2023"
num1 = re.findall(r'\d+',text)
num2 = re.findall(r'[0-9]{2,5}', text)
print(num1)
print(num2)

#find all the alphabets in the text
s = re.findall(r'[a-zA-z]+', text)
print(s)

#find all the symbols in the text
s = re.findall(r'\W+', text)
print(s)

#find all the alphabets and digits
s = re.findall(r'[A-Za-z0-9]+',text)
print(s)

#find email address
text = "My email address is: abc123@def.com"
s = re.findall(r'[A-Za-z0-9]+@[A-Za-z0-9]+\.com', text)
print(s)

#find url
text = "Python home page: https://www.python.org"
s = re.findall(r'https?://.*', text)
print(s)

#find every div tag
html = "aa<div>test1</div>bb<div>test2</div>cc"
res = re.search("<div>.*</div>", html)
print(res.group())

#find first div tag
html = "aa<div>test1</div>bb<div>test2</div>cc"
res = re.search("<div>.*?</div>", html)
print(res.group())

