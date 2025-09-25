#Write a program to create a dictionary of student names and marks, then print students who scored above 75.
students={"devi":80,"Niv":70,"Amal":90,"Amith":60,"Abab":78}
for name,marks in students.items():
    if marks>75:
        print(name,marks)
