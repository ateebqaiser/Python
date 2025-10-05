patients={}
size=int(input("Enter dictionary size : "))
for i in range(size):
    name=input("Enter patient name : ")
    conditions=int(input("Enter number of conditions : "))
    condition_list=[]
    for j in range(conditions):
        condition_name=input("Enter condition : ")
        condition_list.append(condition_name)
    print("AI risks : ")
    diabetes_risk=float(input("Enter diabetes risk : "))
    heart_risk=float(input("Enter heart risk : "))
    cancer_risk=float(input("Enter cancer risk : "))
    patients[f"P00{i+1}"]={
        "name": name,
        "conditions": condition_list,
        "AI_risks": {
            "diabetes_risk": diabetes_risk,
            "heart_risk": heart_risk,
            "cancer_risk": cancer_risk}
    }

#Task 1: Print all patient IDs
print("Patient IDs(keys):", list(patients.keys()))

#Task 2: Print all patient names
print("Patient Names:", list(p["name"] for p in patients.values()))

#Task 3: Print each patient’s conditions
for pdata in patients.values():
    print(f"{pdata['name']}'s conditions: {pdata['conditions']}")

# Task 4: Print AI risk predictions for each patient
for pdata in patients.values():
    print(f"AI risk predictions for {pdata['name']} ")
    for risks,scores in pdata["AI_risks"].items():
        print(f"\t\t{risks}:{scores}")

# Task 5: Add a new condition "Obesity" to John Doe’s condition list
for pdata in patients.values():
    if pdata["name"] == "John Doe":
        pdata["conditions"].append("Obesity")
        print(f"\nUpdated conditions for John Doe: {pdata['conditions']}")

# Task 6: Update Alice Smith’s "heart_risk" score to 0.55
for pdata in patients.values():
    if pdata["name"] == "Alice Smith":
        # pdata["AI_risks"]["heart_risk"] = 0.55
        pdata["AI_risks"].update({"heart_risk":0.55})
        print(f"\nUpdated AI risks for Alice Smith: {pdata['AI_risks']}")

# Task 7: Remove "cancer_risk" from any patient’s AI predictions if it exists
for pdata in patients.values():
    removed = pdata["AI_risks"].pop("cancer_risk", None)
    if removed is not None:
        print(f"\nRemoved cancer_risk for {pdata['name']}")

# Task 8: Add a new patient "P003"
patients.update({
    "P003": {
        "name": "Bob Johnson",
        "conditions": ["Hypertension", "Allergy"],
        "AI_risks": {"diabetes_risk": 0.1, "heart_risk": 0.2}
    }
})

# Task 9: Print all keys and values neatly (formatted report)
print("\n--- Patient Report ---")
for pid, pdata in patients.items():
    print(f"\nPatient ID: {pid}")
    print(f"Name: {pdata['name']}")
    print("Conditions:", ", ".join(pdata["conditions"]))
    print("AI Risk Scores:")
    for risk, score in pdata["AI_risks"].items():
        print(f"  {risk}: {score}")