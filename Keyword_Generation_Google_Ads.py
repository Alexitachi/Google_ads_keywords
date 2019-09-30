# List of words to pair with products
words = ['buy', 'price','discount', 'cheap', 'offer', 'shop']
​
# Print list of words
print(words)

products = ['laptop', 'mobile', 'xbox', 'ps4', 'headphone']
​
# Create an empty list
keywords_list = []
​
# Loop through products
for product in products : 
    # Loop through words
    for word in words :
        # Append combinations
        keywords_list.append([product, product+ ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)

# Load library
import pandas as pd
​
# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)
​
# Print the keywords DataFrame to explore it
print(keywords_df.head())

# Rename the columns of the DataFrame
keywords_df = keywords_df.rename(columns={0: 'Ad Group',1:'Keyword'})

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()
​
# Change criterion type match to phrase
keywords_phrase["Criterion Type"]='Phrase'
​
# Append the DataFrames
keywords_df_final=keywords_df.append(keywords_phrase)
​
​
# Save the final keywords to a CSV file
keywords_df_final.to_csv('keywords.csv',index=False)
# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
