import pandas as pd


df = pd.read_csv('data.csv')

# TUPLE DUPLICATION
# Removes rows that are exact clones across all columns
df = df.drop_duplicates()

# SYNTACTIC INCONSISTENCY
# Standardizes 'Stock_Status' to Title Case
df['Stock_Status'] = df['Stock_Status'].str.title().str.strip()
#Standardizes publisher 
df['Publisher'] = df['Publisher'].str.strip()

# SEMANTIC INCONSISTENCY
# Groups by the Key (Product_ID) and resolves conflicting values
# Note: Pandas renames the second 'Price' column to 'Price.1' automatically
# The as_index=False parameter is telling pandas: don't treat row numbers as actual data
df_cleaned = df.groupby('Product_ID', as_index=False).agg({
    'Game_Title': 'first',
    'Game_Name': 'first',
    'Platform': 'first',
    'Price': 'max',            # Resolves price conflicts by picking the highest
    'Price.1': 'max',          # Resolves conflicts in the second price column
    'Price_With_Tax': 'max',   
    'Metacritic_Score': 'mean', # Averages conflicting scores
    'User_Rating': 'mean',      # Averages conflicting ratings
    'Stock_Status': 'first',    
    'Publisher': 'first'        
})

# OUTPUT THE CLEANED DATA
# Save the results to a file
df_cleaned.to_csv('cleaned_data_1.csv', index=False)

# Display the sample to verify
print("Cleaned Data Sample:")
print(df_cleaned.head())