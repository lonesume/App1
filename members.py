user = input("Enter a new member:")
file = open("members.txt", "a")
file.write(user)
file.close()