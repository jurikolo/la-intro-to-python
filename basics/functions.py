print("Docs: https://docs.python.org/3/tutorial/controlflow.html#defining-functions")

def jk_sum(a, b):
    print("Inside jk_sum function")
    return a+b

a = 1
b = 2
print(f"{a} + {b} = {jk_sum(a, b)}")

print()
def jk_details(name, surname, certificate):
    return f"{name} {surname} has {certificate} certificate"

print("Common way to pass variables in a function")
print(jk_details("Jurijs", "Kolomijecs", "AWS Certified Solutions Architect"))
print("Alternate way to pass variables in a function")
print(jk_details(certificate="AWS Certified Solutions Architect", name="Jurijs", surname="Kolomijecs"))

print()
def jk_driving_age(age, driving_age=18):
    print(f"Driving age is {driving_age}")
    if age >= driving_age:
        return "Can drive"
    else:
        return "Can't drive"

print(jk_driving_age(15))
print(jk_driving_age(15, 12))