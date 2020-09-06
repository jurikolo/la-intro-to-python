print("Docs: https://docs.python.org/3/glossary.html#term-decorator")
print("Part 1, learn how to pass args into function")
def inspect(func, *args):
    print(f"Running {func.__name__}")
    val = func(*args)
    print(f"{func.__name__} execution result: {val}")
    return val

def combine(a, b):
    return a + b

inspect(combine, 1, 2)

print()
print("Part 2, learn how to actually use decorators")
def inspect2(func):
    def wrapped_function(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"{func.__name__} execution result: {val}")
        return val

    return wrapped_function

@inspect2
def combine2(a, b):
    return a + b

combine2(1, 2)

print()
print("Part 3, learn how to use class decorators")
class User:
    base_url = "https://example.com/api"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url + "?" + query_string

    @staticmethod
    def name():
        return "Jurijs Kolomijecs"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

print(User.name)
print(User.name())
print(User.query("test"))
user = User("Name1", "Surname1")
print(user.base_url)
print(user.full_name)
user.first_name = "Name2"
print(user.full_name)