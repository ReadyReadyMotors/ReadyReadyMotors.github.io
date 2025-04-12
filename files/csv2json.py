import ast
# Load the newly uploaded inventory.csv
new_csv_path = Path("/mnt/data/inventory.csv")
new_df = pd.read_csv(new_csv_path)

# Preview the Images_list column to check for issues
new_df['Images_list'].head(10)


# Clean and safely parse the Images_list column
new_df['Images_list'] = new_df['Images_list'].apply(clean_and_parse_list)

# Convert to JSON format
new_inventory_json = new_df.to_dict(orient="records")

# Save to JSON file
new_json_path = new_csv_path.with_suffix(".json")
with open(new_json_path, "w") as f:
    json.dump(new_inventory_json, f, indent=2)

new_json_path.name




# # Clean and safely parse each list using ast.literal_eval
# def clean_and_parse_list(val):
#     try:
#         val = val.strip().rstrip('"').strip()  # Remove trailing quote and whitespace
#         return ast.literal_eval(val)
#     except Exception:
#         return []

# df['Images_list'] = df['Images_list'].apply(clean_and_parse_list)

# # Convert to list of dictionaries
# inventory_json = df.to_dict(orient="records")

# # Save as JSON
# json_path = csv_path.with_suffix(".json")
# with open(json_path, "w") as f:
#     json.dump(inventory_json, f, indent=2)

# json_path.name
