# This is a sample Python script.


def func1(data_in,key_in):
    key_found = 0
    out = recursive_func1(data_in, key_in, key_found)
    if(out['key_found']==1):
        return out['value']
    else:
        return "Key not found"


def recursive_func1(data_in,key_in,key_found):
    out = {}
    for key,value in data_in.items():
        if(key == key_in):
            key_found = 1
        out["key_found"] = key_found
        if(isinstance(value,dict)):
            out = recursive_func1(value,key_in,key_found)

        else:
            out["value"] =  value

    return out


#Main script for input and output
nested_data = {"x":{"y":{"z":"d"}}}
key = "x"
print("Result= " + func1(nested_data,key))
