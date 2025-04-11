from scholarly import scholarly
import pandas as pd

# Search for your topic
search_query = scholarly.search_pubs('emerging authentication techniques')

# Extract publication years
years = []
for publication in search_query:
    if 'bib' in publication and 'pub_year' in publication['bib']:
        years.append(publication['bib']['pub_year'])

# Count publications per year
publications_per_year = pd.Series(years).value_counts().sort_index()

# Display the results
print(publications_per_year)

# Save to a CSV file
publications_per_year.to_csv('publications_per_year.csv')