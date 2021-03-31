#Melker Ölander Te19d



x = int(input("Ange den första sidan"))
y = int(input("ange den andra sidan"))

area = x*y

print(f"rektangelns area är {area}")
if x == y:
    print(f"eftersom rektangelns sidor är lika långa så är det en kvadrat")

for i in range(1,11):
        volym = area*i
        print(f"när höjden är {i} så är volymen {volym}")


'''
uppgift 2
'''
while true:
    x = int(input("Ange den första sidan"))
    y = int(input("Ange den andra sidan"))

    area = x*y

    print(f"rektangelns area är {area}")
    if x == y:
        print(f"eftersom rektangelns sidor är lika långa så är det en kvadrat")

    if x == y:
        print(f"eftersom ")