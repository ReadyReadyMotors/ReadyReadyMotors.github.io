# Re-run the conversion process after code environment reset
import pandas as pd
import json
from pathlib import Path

# Reload the JSON file
json_path = Path("/mnt/data/inventory.json")
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(data)

# Convert Images_list to a comma-separated string
df['Images_list'] = df['Images_list'].apply(lambda x: ','.join(x) if isinstance(x, list) else '')

# Save as CSV
csv_path = json_path.with_suffix('.csv')
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

csv_path.name
