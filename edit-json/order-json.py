import json


file_path = 'edit-json/filtered_data.json'
with open(file_path, 'r') as file:
    data = json.load(file)

sorted_data = sorted(data, key=lambda x: x["number"])

ordered_data = []
# Print the data in the desired format
for index, entry in enumerate(sorted_data, start=1):
    ordered_data.append(f"{index}. {entry['body']}")


   

output_file = 'edit-json/ordered_data.json'
with open(output_file, 'w') as file:
    json.dump(ordered_data, file, indent=4)

print("Filtered JSON file saved to", output_file)