import json


file_path = 'edit-json/ordered_data.json'
with open(file_path, 'r') as file:
    data = json.load(file)

formatted_data = [entry.split("\n", 1)[0] for entry in data]



   

output_file = 'edit-json/formatted_data.txt'
with open(output_file, "w") as file:
    for entry in formatted_data:
        file.write(entry + "\n")

print("Filtered JSON file saved to", output_file)

output_file_name = "formatted_data.txt"

# Write the formatted data to the text file
with open(output_file_name, "w") as file:
    for entry in formatted_data:
        file.write(entry + "\n")