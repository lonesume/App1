# import random
# countries = ["USA", "India", "Germany", "UK"]
# country = "UKmem" #random.choice(countries)
# print(f"Value of country: <{country}>")

# match  country:
#     case 'India':
#         print("namaste")
#     case 'USA':
#         print("Hello!")
#     case 'Germany':
#         print("Hallo")
#     case 'UK':
#         print("What up mandem!")
#     case 'London':
#         print("What up mandem!")

# domain = "coolmail.com"
# members = ["john smith", "sen plakay", "dora ngacely"]
# emails = []

# members_title_case = []


# for member in members:
#     # print(member.title())
#     members_title_case.append(member.title())
#     email = member.replace(" ", ".")
#     email = email + "@"+ domain
#     # print(email)
#     emails.append(email)
# print(emails)


# # print(f"members (after) {members}")
# # print(f"members_title_case (after) {members_title_case}")

# colors = [11, 34, 98, 43, 45, 54, 54]
# for color in colors:
#     print(color)
# buttons = ["cancel", "reply", "submit"]
 
# for i in buttons:
#     break
# print(i.capitalize())
def dollars_to_euros():
    dollars = float(input("Enter Dollar amount:"))
    euros = dollars * 2
    print("Euros:", euros)

haystack = ['John', 'Sen', 'Lisa']
haystack_lower = [hay.lower() for hay in haystack]

haystack_lower2 = []
for hay in haystack:
    haystack_lower2.append(hay)


print("hs_lower:", haystack_lower)
needle = (input("Enter a name :")) 
needle_lower = needle.lower()

# old, case sensitive
# print(haystack.index(needle)+1)

# new, case in-sensitive
print(haystack_lower.index(needle_lower)+1)


# for i in range(len(ranking)):
#     name = ranking[i]
#     if name == enter_name :
#         print(i+1)




    