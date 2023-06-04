import copy


#EXERCISES

animals = ['cat','dog', 'bird']
animals.insert(1, 'snake')
print(animals)
animals.remove('bird')
print(animals)

for i, x in enumerate(animals):
  print(i, x)

l =[10, 20 ,30]

l.sort()
print(l)

l.reverse()
print(l)

squares = [x*2 for x in animals]
print(squares)

l2 =[[1,2],[4,5]]
print(l2[1][0])

l3=[0,1,2,3,4,5]
print(l3[: :2])
print(l3[1:4:2])


t = (1, [1,2], 'python')
print(t)
print(type(t))

t1 =(5,)
print('t1', type(t1))

t2 = (1,2,3)
print(t2[2])

x = {'food': 'Spam', 'quantity':4, 'color': 'pink'}
x2 = dict(food = 'Spam', quantity = 4, color = 'pink')
x3 = dict([("food", "spam"),("quantity", 4),("color","pink")])

print(x)
print(x2)
print(x3)

print((x.get("food")),x.values())
print((x2.get("quantity")),x2.keys())
print((x3.get("color")),x3.items())

sample_set = {'Prince', 'Techs'}
sample_set2 = set(['Todd','Techs'])
print(sample_set)
print(sample_set2)

print('Data' in sample_set)
print('Techs' in sample_set2)

sample_set.add('Adam')
print(sample_set)
print(len(sample_set))
sample_set.remove('Adam')
print(sample_set)


list2 = [1,3,1,5,3]
print(list(set(list2)))
print(list2[4])

sample_set = {'Prince', 'Techs'}
sample_set = frozenset(sample_set)
sample_set.add('cat')

a = [1,2,3,[4,5]]
b = a.copy()
b[0]= 99
print(a)
print(b[0])


b=copy.deepcopy(a)
b[3][0]=99
print(a)
print(b)

