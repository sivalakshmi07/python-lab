#Write a program to create a dictionary that stores an integer, float, string, list, tuple, set, and another dictionary as values, then print each key and its value.
data={"int":10,"float":3.14,"string":"Hello","list":[1,2,3],"tuple":(4,5,6),"set":{7,8,9},"dict":{"a":1,"b":2}}
for key,value in data.items():
    print(key,value)