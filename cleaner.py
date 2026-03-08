import pandas as pd

# 1. Load the messy data
# This creates a "DataFrame" (basically a digital spreadsheet)
df = pd.read_csv('raw_leads_sample.csv')

# 2. Fix the names
# This turns "JOHN DOE" or "jane smith" into "John Doe"
df['first_name'] = df['first_name'].str.capitalize()
df['last_name'] = df['last_name'].str.capitalize()

# 3. Clean the company names
# This removes hidden spaces at the start or end (like "  Meta  ")
df['company'] = df['company'].str.strip()

# 4. Remove Duplicates
# If the same person is in the list twice, it keeps only the first one
df = df.drop_duplicates()

# 5. Save the result
# This creates a brand new, perfect CSV file
df.to_csv('cleaned_leads_final.csv', index=False)

print("Success! Your leads are now CRM-ready.")
