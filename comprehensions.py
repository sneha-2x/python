print('list...')

a = [1,2,3,4,5]
odd = [i for i in a if i%2 != 0]
print(odd)

#additive inverse
num = [2,-4,1,-1]
lst = [-1 * a for a in num]
print(lst)

print('set...')
s = {1, 2, 3, 4, 5, 3}
print(s)
even = {i for i in s if i % 2 == 0}
print(even)

n = [1,-1,2,-2,3,-3]
print({i**2 for i in n})


print('dict...')
city = ['hyderabad','chennai','bengalore']
state = ['telangana','tamil nadu','karnataka']
dic = {c:s for c,s in zip(city,state)}
print(dic)

integer = range(1,11)
binary = []
for i in integer:
    bnr = bin(i)
    binary.append(bnr)

binary_dict = {i:b for i,b in zip(integer,binary)}
print(binary_dict)
