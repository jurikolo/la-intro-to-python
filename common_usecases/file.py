print("Docs https://docs.python.org/3/library/functions.html#open")
print("Create a file for read and write. Overwrite existing file")
my_file = open('cities.txt', 'w+')
my_file.write("Jurmala\n")
my_file.write("Katlakalns\n")
my_file.writelines([
    "Riga\n",
    "Daugavpils\n"
    "Ventspils\n"
])
my_file.close()

print("Open a file for reading and print it")
my_file = open('cities.txt', 'r')
print(my_file.read())
print("Move cursor back to the start of the file to print it again")
my_file.seek(0)
print(my_file.read())
my_file.close()

print("Alternate option to get rid of closing the file manually, use \"with\" option")
with open('cities.txt', 'w+') as my_file:
    my_file = open('cities.txt', 'w+')
    my_file.write("Jurmala\n")
    my_file.write("Katlakalns\n")
    my_file.writelines([
        "Riga\n",
        "Daugavpils\n"
        "Ventspils\n"
    ])

with open('cities.txt', 'r') as my_file:
    print(my_file.read())
    print("Move cursor back to the start of the file to print it again")
    my_file.seek(0)
    print(my_file.read())
