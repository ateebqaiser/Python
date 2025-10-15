customers={}
size=int(input("Enter number of customers: "))

# Input customer details
for i in range(size):
    name = input("Enter customer name: ")
    # Accounts
    acc_count = int(input("Enter number of account types: "))
    accounts = {}
    for j in range(acc_count):
        acc_type = input("Enter account type (e.g. savings/current): ")
        balance = float(input(f"Enter balance for {acc_type}: "))
        accounts[acc_type] = balance
    
    # AI Risks
    print("Enter AI Risk Scores:")
    fraud_risk = float(input("Fraud Risk: "))
    loan_default_risk = float(input("Loan Default Risk: "))
    credit_risk = float(input("Credit Risk: "))
    
    # Add to main dictionary
    customers[f"C00{i+1}"] = {
        "name": name,
        "accounts": accounts,
        "AI_risk_scores": {
            "fraud_risk": fraud_risk,
            "loan_default_risk": loan_default_risk,
            "credit_risk": credit_risk
        }
    }

# Task 1: Print all customer IDs
print("\nCustomer IDs:", list(customers.keys()))

# Task 2: Print all customer names
print("Customer Names:", [c["name"] for c in customers.values()])

# Task 3: Print each customer’s account balances
for cdata in customers.values():
    print(f"\n{cdata['name']}'s Accounts:")
    for acc, bal in cdata["accounts"].items():
        print(f"  {acc}: {bal}")

# Task 4: Print AI risk scores for each customer
for cdata in customers.values():
    print(f"\nAI Risk Scores for {cdata['name']}:")
    for risk, score in cdata["AI_risk_scores"].items():
        print(f"  {risk}: {score}")

# Task 5: Add new account "fixed_deposit" = 50000 for one customer
for cdata in customers.values():
    if cdata["name"] == "John Doe":  # change name if needed
        cdata["accounts"]["fixed_deposit"] = 50000
        print(f"\nAdded fixed_deposit for {cdata['name']}: {cdata['accounts']}")

# Task 6: Update one customer’s "loan_default_risk"
for cdata in customers.values():
    if cdata["name"] == "Alice Smith":  # change name if needed
        cdata["AI_risk_scores"]["loan_default_risk"] = 0.45
        print(f"\nUpdated loan_default_risk for {cdata['name']}: {cdata['AI_risk_scores']}")

# Task 7: Remove "fraud_risk" using pop()
for cdata in customers.values():
    removed = cdata["AI_risk_scores"].pop("fraud_risk", None)
    if removed is not None:
        print(f"\nRemoved fraud_risk for {cdata['name']}")

# Task 8: Add new customer using update()
customers.update({
    "C003": {
        "name": "Bob Johnson",
        "accounts": {"savings": 12000, "current": 8000},
        "AI_risk_scores": {"loan_default_risk": 0.2, "credit_risk": 0.3}
    }
})

# Task 9: Print formatted banking report
print("\n--- Banking Report ---")
for cid, cdata in customers.items():
    print(f"\nCustomer ID: {cid}")
    print(f"Name: {cdata['name']}")
    print("Accounts:")
    for acc, bal in cdata["accounts"].items():
        print(f"  {acc}: {bal}")
    print("AI Risk Scores:")
    for risk, score in cdata["AI_risk_scores"].items():
        print(f"  {risk}: {score}")
