# clear function

sampleList=[1,2,3,4,56,7]

print("sampleList",sampleList)

del sampleList[0:3]
print("sampleList after del",sampleList)


#index

vowels=['a','e','i','o','u']

print("index of i:",vowels.index('i'))


#extend

languages=['marathi','hindi']

print("languages",languages)

other=["english"]
other.extend(languages)

print("other",other)


# difference between append and extend

a=[1,2]
b=[3,4]
c=(8,9)

a.append(c)
print("append",a)

b.extend(c)
print("extend",b)


#revese

list=[1,2,3,4,5,6]

list.reverse()

print("reversed list",list)

#count
list=[1,2,4,9,10,10]
print("list count",list.count(10))

#insert
color=['red', 'green']
color.insert(0,'black')
print("color",color)