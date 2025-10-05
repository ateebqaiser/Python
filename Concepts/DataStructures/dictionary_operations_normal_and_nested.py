# Dictionary: An ordered collection of items, accessed by keys (like names, IDs, etc.).
# Key / value
# dupicate values not allowed
# Syntax: dictionary = ["key":value]

# Dictionary Creation
patient_dictionary={"id":101,
                    "name":"Raima",
                    "age":39,
                    "disease":"sugar",
                    "med_History":["diabetes","BP","thyroid"]
}

# Print Entire Dictionary
print(patient_dictionary)

# Access Value by Key ("name")
print(patient_dictionary["name"])

# Add New Key-Value Pair (Address)
patient_dictionary["Address"]="H no 69"

print(patient_dictionary)

# Convert Dictionary Keys to List
list1 = list(patient_dictionary.keys())   
print(list1)

# Convert Dictionary Values to List
list2=list(patient_dictionary.values())   
print(list2)

# Update Dictionary Value (Change "name" to "Ali")
patient_dictionary.update({"name":"Ali"})
print(patient_dictionary)

# Remove Key by pop(),Removes the key "name" and its value from the dictionary.
patient_dictionary.pop("name")
print(patient_dictionary)

# Remove Last Item by popitem(),Removes the last inserted key-value pair from the dictionary.
patient_dictionary.popitem()
print(patient_dictionary)

# Find Length of Dictionary, Calculates the number of key-value pairs currently in the dictionary.
length=len(patient_dictionary)
print("Length : ",length)

# Create a Copy of Dictionary,Creates a shallow copy of patient_dictionary so that changes to the original won’t affect the copy.
backup_copy=patient_dictionary.copy()
print("Backup : ",backup_copy)

# Clear All Items,Removes all items from the dictionary (dictionary becomes empty {}).
patient_dictionary.clear()
print(patient_dictionary)

# Delete Entire Dictionary,Deletes the dictionary completely from memory. After this, you cannot use patient_dictionary anymore.
del patient_dictionary


# Python Dictionary Operations: Creation, Access, Modification, and Management
new_patients_dictionary = []
size = 4 

for i in range(size):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    new_patients_dictionary[f"patient{i+1}"] = {
       "name":name,
        "age": age,
        "disease": disease
}

print("New Patients Dictionary:", new_patients_dictionary)

# Python Dictionary Operations: Creation, Access, Modification, and Management with list

# new_patients_dictionary = []
# size = 2

# for i in range(size):
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     disease = input("Enter disease: ")
#     new_patients_dictionary.append(
#     {  "patient" : f"patient{i+1}",
#        "name":name,
#         "age": age,
#         "disease": disease
# })

#Nested Dictionary

nested_dictionary={
    "P001":{
        "name":"zain"
    },
    "P002":{
        "name":"ali"
    }
}
print(nested_dictionary)