#Write a program to count words,lines and characters in a user-provided sentence.
word=input("Enter A Sentence: ")
numofsent=len(word.split("."))
print("Number of Sentence = ",numofsent)
countword=word.split(" ")
print("Number of Lines = ",len(countword))
print("Number of Characters = ",len(word))