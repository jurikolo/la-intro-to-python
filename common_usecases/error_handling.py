file_name = "teams.txt"
print("Docs: https://docs.python.org/3/reference/compound_stmts.html#the-try-statement")
print("Following statement works once, when there is no file on disk. Fails for the second time")
my_file = open(file_name, "x")
my_file.write("Pardaugava\n")
my_file.close()

print("Let's have a try / catch for the second attempt")
try:
    my_file = open(file_name, "x")
    my_file.write("Pardaugava\n")
    my_file.close()
except FileExistsError as error:
    print(f"File {file_name} already exists")
except:
    print("Something went totally wrong")
else:
    print("File processed successfully")
finally:
    print("Program execution completed")