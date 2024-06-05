filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for item in filenames:
    file = open(item, "a")
    file.write("hello")
    file.close()