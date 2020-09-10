import json

# TODO: implement conversion to JSON
def export_to_json(users, path):
    print("In export_to_json function")
    print(f"Users: {users}, path: {path}")
    return None

def export_to_csv(users, path):
    if path:
        output_file = open(path, 'w+')
        output_file.write("name,id,home,shell\n")
        for user in users:
            output_file.write(f"{user['user']},{user['id']},{user['home']},{user['shell']}\n")
        output_file.close()
    else:
        print("name,id,home,shell")
        for user in users:
            print(f"{user['user']},{user['id']},{user['home']},{user['shell']}")