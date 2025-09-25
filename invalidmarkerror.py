name=input("Enter name:")
try:
    mark=int(input("Mark:"))
    if(mark<0 or mark>100):
        raise ValueError("Mark should'nt be <0 or >100")
except ValueError as e:
    print(e)