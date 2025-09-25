#Write a program to accept a list of numbers and print all numbers greater than the average.
a = list(map(int, input("Enter the numbers: ").split()))
avg = sum(a) / len(a)
print("Numbers greater than average:")
for i in a:
    if i > avg:
        print(i)