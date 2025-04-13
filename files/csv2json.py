import pandas as pd
import json
from pathlib import Path

# Load the CSV file
csv_path = Path("/mnt/data/inventory.csv")
df = pd.read_csv(csv_path)

# Convert 'Images_list' string back to a list
df['Images_list'] = df['Images_list'].apply(lambda x: [img.strip() for img in str(x).split(',')] if pd.notna(x) else [])

# Convert DataFrame to list of dictionaries
data_json = df.to_dict(orient='records')

# Save as JSON
json_path = csv_path.with_suffix('.json')
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(data_json, f, ensure_ascii=False, indent=2)

json_path.name
