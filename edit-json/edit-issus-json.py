import json


file_path = 'edit-json/ci-pp5-issues.json'
with open(file_path, 'r') as file:
    data = json.load(file)

new_data = []
for entry in data:

    split_title = entry["title"].split(" ")

    if split_title[0] == "USER":

        new_entry = {
            "number": entry["number"],
            "body": entry["body"]
        }

        new_data.append(new_entry)

output_file = 'edit-json/filtered_data.json'
with open(output_file, 'w') as file:
    json.dump(new_data, file, indent=4)

print("Filtered JSON file saved to", output_file)