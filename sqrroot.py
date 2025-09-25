#list with 5 values find sqaure of each list and print a list with all these values
a=[1,2,3,4]
print(set(a))
for i in a:
    a.append(math.sqrt(a))
print(a)