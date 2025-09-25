#Write a program to create a nested dictionary of student names and their subject marks, then display each student’s details.
students={"Devi":{"Math":95,"Physics":92},"Sheb":{"Math":85,"Physics":90},"Niv":{"Math":70,"Physics":65}}
for name,marks in students.items():
   print(name)
for subject,score in marks.items():
    print(subject,score)