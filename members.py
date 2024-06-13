# try:
#     total_value = float(input("Enter total value: "))
#     value = float(input("Enter value: ")) 
#     total = value/total_value *100
#     print(f"{total}%")
# except ValueError :
#     print("You need to enter a number.")
# except ZeroDivisionError:
#     print("Total value cannot be 0")
try :
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError :
    print("Name is not found")
