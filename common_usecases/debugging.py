import pdb

print("Docs: https://docs.python.org/3/library/pdb.html")
print("Instead of importing pdb and setting trace points, you can run the script with '-m pdb'")
print("Type variable names inside pdb to see variable content")
print("Type 'h' or 'help' for a list of available commands")
def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace()
        output_values.append(func(values[index]))
        index += 1
    return output_values

def add_one(val):
    return val + 1

print(map(add_one, list(range(10))))