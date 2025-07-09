#--------------------------------------------
# filename: friends_json.py
# autor: Nikhil Schmelzle
# last edit: 09.07.2025 (DDMMYYYY)
#--------------------------------------------
import json

# Initial list of friends
friends = ["Wolf", "Dennis", "Patrick", "Benni", "Mega"]

try:
    # Save the original list to the file in JSON format
    with open("friends.json", "w", encoding="utf-8") as file:
        json.dump(friends, file, indent=4, ensure_ascii=False)

    # Read the list back from the file into a new variable
    with open("friends.json", "r", encoding="utf-8") as file:
        friends_from_file = json.load(file)

    # Add a new friend to the list read from file (original list remains unchanged)
    friends_from_file.append("David")

    # Overwrite the file with the updated list
    with open("friends.json", "r+", encoding="utf-8") as file:
        json.dump(friends_from_file, file, indent=4, ensure_ascii=False)
        file.truncate()  # Remove leftover content from the previous version

except Exception as e:
    print("An error occurred while handling the file:", e)