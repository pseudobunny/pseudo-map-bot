from .json_utils import write_to_json, read_from_json

def bal_set(name, amount):

    try:
        data = read_from_json()
    except:
        write_to_json({})
        data = read_from_json()
        
    if name in list(data.keys()):
        data[name] = amount
    else:
        data.update({name: amount})

    write_to_json(data)