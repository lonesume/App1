# todos = []

# while True:
#     user_action = input("Type add, show, or exit : ").strip()

#     match user_action :
#         case 'add':
#             todo = input("Enter a todo:").strip() 
#             todos.append(todo)
#             print(f"\nTodo '{todo}' added to list of todos! :)\n")
#         case 'show':
#             for item in todos:
#                 print(item)
#         case 'exit':
#             break
#         case _:
#             print("Invalid option \n Please try again")

# print("Thank You!")
def coding_ex_1():
    filenames = ['document', 'report', 'presentation']
    for index, item in enumerate(filenames):
     upper = item.capitalize()
     row = f"{index}-{upper}.txt"
     row2 = "{0}-{1}".format(index, upper)
    print (index, upper, ".txt")
    print(row)

# ips = ['100.122.133.105', '100.122.133.111']
# user_action = int(input("Enter the index of the ip you want:"))
# print(f"You chose {ips[user_action]}")
# print(f"ips[0] <{ips[0]}>")
# print(f"ips[0][0] <{ips[0][0]}>")

# # expects 14

# print(f"[using counting] The last number of the first string in ips is: <{ips[0][14]}>")

# first_ip = ips[0]
# last_index = len(first_ip) - 1 
# print(f"[using len()] The last number of the first string in ips is: <{first_ip[last_index]}>")
# print(f"[using -1] The last number of the first string in ips is: <{first_ip[-2]}>")


# # Task: Reverse the string
# string = "Brian"

# # Step 1: split string into list of chars
# split_chars = list(string)


# # Step 2: Devise algo to reverse 
# reversed_string = ""

# length_of_string = len(split_chars)

# for i in range(length_of_string-1, -1, -1):
#     reversed_string +=  split_chars[i]


# reversed_string2 = string[::-1]

# # Step 2.something: index into list, move it over



# # Step 3 print reversed
# print(f"{string} reversed is '{reversed_string}'")
# print(f"{string} reversed is '{reversed_string2}'")


# names = ["john smith", "jay santi", "eva kuki"]
# namescap = [word.title()for word in names]
# print(namescap)

# temperatures = ['10', '12', '14']
# temp2 ="\n".join(temperatures)
 
# file = open("file.txt", 'w')
 
# file.write(temp2)

user_input = input("Enter a password:")
password = [user_input]
pass_count = [len(i)for i in password]
if len(pass_count[0:]):
   print("Strong Password")
if len(pass_count[0:7]):
    print('Password is weak')
   











   







