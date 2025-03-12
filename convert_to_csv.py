import json
import csv

# Convert JSON to CSV
with open("raw_data.json", "r") as json_file:
    data = json.load(json_file)

with open("processed_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "userId", "title", "body"])  # Headers

    for item in data:
        writer.writerow([
            item["id"],
            item["userId"],
            item["title"],
            item["body"]
        ])
print("CSV created successfully!")
