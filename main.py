# Simple Tech Service Centre Log System (INT108 Python Project)
records = []

while True:
    print("\n--- TECH SERVICE CENTRE ---")
    print("1. Add Repair Entry")
    print("2. View All Entries")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        name = input("Customer Name: ")
        device = input("Device Name: ")
        issue = input("Issue Details: ")
        records.append({"name": name, "device": device, "issue": issue})
        print("Entry saved successfully!")
    elif choice == "2":
        print("\n--- Current Repair List ---")
        for i, r in enumerate(records, 1):
            print(f"{i}. {r['name']} | {r['device']} | {r['issue']}")
    elif choice == "3":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, try again.")
