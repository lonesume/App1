filenames = ['a.txt', 'b.txt', 'c.txt']
for item in filenames:
    file = open(item, "r")
    print(file.read())
    file.close()