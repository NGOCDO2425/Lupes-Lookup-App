import json

# Define the filename for the birthday data
filename = "birthday.json"

# Load existing data or create an empty dictionary if the file doesn't exist
try:
    with open(filename, "r") as file:
        data = json.load(file)  # Load existing JSON data
        if isinstance(data, list):  # Convert list to dictionary if necessary
            birthdays = {entry["name"]: entry["birthday"] for entry in data}
        else:
            birthdays = data
except (FileNotFoundError, json.JSONDecodeError):  
    birthdays = {}  # Start fresh if the file is missing or corrupted
# Get user input
name_input = input("Enter a name (or part of a name): ").strip()

# Flag to track if we found a match
found = False

# Check for an exact match first
if name_input in birthdays:
    print(f"{name_input}'s birthday is {birthdays[name_input]}")
    found = True
else:
    # Find partial matches using a for-loop
    print("Searching for partial matches...")
    for name, bday in birthdays.items():
        if name_input.lower() in name.lower():  # Case-insensitive substring match
            print(f"{name}: {bday}")
            found = True

# If no matches were found, ask the user to add a new entry
if not found:
    print("Birthday unknown")
    add_entry = input("Would you like to add this person to the birthday list? (yes/no): ").strip().lower()

    if add_entry == "yes":
        new_birthday = input(f"Enter {name_input}'s birthday (YYYY-MM-DD): ").strip()
        birthdays[name_input] = new_birthday  # Store the name exactly as input
        
        # Save the updated dictionary back to JSON
        with open(filename, "w") as file:
            json.dump(birthdays, file, indent=4)

        print(f"{name_input} has been added to the birthday list.")
