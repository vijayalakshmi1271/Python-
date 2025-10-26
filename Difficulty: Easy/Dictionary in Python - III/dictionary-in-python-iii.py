# insert into dictionary
def insert_dict(query, dict):
    dict[query[1]] = query[2]

# deleting from dictionary
def del_dict(query, dict):
    if query[1] in dict:
        del dict[query[1]]
    else:
        return -1
          
# print marks of required name
def print_dict(key, dict):
    if key in dict.keys():
        print(f"Marks of {key} is {dict[key]}")
    else:
        print("-1")

 