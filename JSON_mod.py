import json

'''
List of Methods:
    1. Delete JSON object
    2. Add to JSON file
    3. Modify JSON object(Delete previous JSON object then add new JSON object)
'''


def manual_data(json_format):
    newData = {}
    if json_format == "assignments":
        newData["permissionSet"] = input("Enter Permission Set Name")
        newData["groupName"] = input("Enter Group Name")
        newData["target"] = input("Enter Target ID")
    elif json_format == "permissionSets":
        newData["permissionSetName"] = input("Enter Permission Set Name")
        newData["managedPolicies"] = input("Enter Managed Policy Arn(Optional)")
        newData["customPolicy"] = input("Enter Inline Policy JSON File Name(Optional)")
        newData["description"] = input("Enter a description for the permission set(Optional)")
        newData["sessionDuration"] = input("Enter the session duration for the permission set(Optional)")
    return newData


def delete_json(data, file_name, json_format, manual):
    if manual == "1":
        newData = manual_data(json_format)
    elif manual == "2":
        new_filename = input("Enter JSON object file that you want to delete(i.e. 'object_removal.json'): ")
        with open(new_filename, "r") as new_file:
            newData = json.load(new_file)
            new_file.close()
    else:
        print("Invalid input option")

    #Removing JSON object to file
    for idx, obj in enumerate(data[json_format]):
        if obj == newData:
            data[json_format].pop(idx)
            print("Successfully deleted JSON object")
            with open(file_name, "w") as file:
                json.dump(data, file, indent=4)
                print(data)
            return

    print("Error: JSON object was not found")
    

def add_json(data, file_name, json_format, manual):
    if manual == "1":
        newData = manual_data(json_format)
    elif manual == "2":
        new_filename = input("Enter new JSON object file that you want to add(i.e. 'object_addition.json'): ")
        with open(new_filename, "r") as new_file:
            newData = json.load(new_file)
            new_file.close()
    else:
        print("Invalid input option")

    #Adding new JSON object to file
    data[json_format].append(newData)
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
        file.close()
        print("Successfuly added JSON Object")
        print(data)


def main():
    method_description = """
    List of Methods: 
    1. Add to JSON file 
    2. Delete JSON object
    """
    print(method_description)

    method_num = input("Enter a number corresponding to the method you would like to use(i.e. '1'): ")
    file_name = input("Enter a JSON file name you would like to modify(i.e. 'assignments.json'): ")
    try: 
        file = open(file_name, "r")
    except OSError:
        print("Error: Could not open/read file:", file_name)
        return 
    
    data = json.load(file)
    if "assignments" in data:
        json_format = "assignments" 
    elif "permissionSets" in data:
        json_format = "permissionSets"
    else:
        print("Error: Original JSON object formatting is invalid")
    file.close()

    manual = input ("Input Options:\
                    1. Manually Enter Data \
                    2. Use JSON file as input")

    if method_num == "1":
        add_json(data, file_name, json_format, manual)
    elif method_num == "2":
        delete_json(data, file_name, json_format, manual)
    # elif method_num == "3":
    #     delete_json(data, file_name, json_format)
    #     add_json(data, file_name, json_format)
    #     print("Successfully modifed JSON object")
    else:
        print("Error: Invalid method number")
        return

    
if __name__ == '__main__':
    main()
