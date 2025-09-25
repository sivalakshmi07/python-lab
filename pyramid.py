#Write a program to print a pyramid of stars using for loop.
rows=5
for i in range(1,rows+1):
    print(" "*(rows-i)+"*"*(2*i-1))