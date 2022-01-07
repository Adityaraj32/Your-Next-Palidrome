number_1 = int(input("Enter The First Number: "))
import copy
add = 0
# while number_1.reverse() == number_1:
while True:
    add+=1
    number_1+=1
    copy = copy.deepcopy(number_1)
    if number_1 < 10:
        number_1+(number_1-10)
    elif str(number_1) == str(number_1)[::-1]:
        print(f"The {copy} Next Paildrome is {add+int(copy)}") 
        print(copy)
        print(number_1)
        break
    continue