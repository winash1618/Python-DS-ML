"""
The goal of this exercise is to implement a function that will return a dictionary of dictionaries giving the number and type of medals for each year during which the participant
won medals.
import pandas as pd

data = pd.DataFrame({
    'name': ['sravan', 'ojaswi', 'bobby', 'rohith',
             'gnanesh', 'sravan', 'sravan', 'ojaswi'],
    'age': [11, 23, 23, 21, 21, 21, 23, 21]
})

# Group data by 'name' and 'age'
grouped_data = data.groupby(['name', 'age'])

# Initialize a nested dictionary to store the counts
count_dict = {}

# Loop through each group and count the occurrences
for (name, age), group in grouped_data:
    if name not in count_dict:
        count_dict[name] = {}
    count_dict[name][age] = len(group)

print(count_dict)
"""

def how_many_medals(df, name):
    """Write a function how_many_medals that takes two arguments:
    • a pandas.DataFrame which contains the dataset,
    • a participant name.
    The function returns a dictionary of dictionaries giving the number and type of medals
    for each year during which the participant won medals. The keys of the main dictionary are the Olympic games years. In each year’s dictionary, the keys are ’G’, ’S’, ’B’
    corresponding to the type of medals won (gold, silver, bronze). The innermost values
    correspond to the number of medals of a given type won for a given year.

    Args:
        df (pandas.DataFrame): dataset
        name (string): participant name
    """
    grouped_data = df[df['Name'] == name].dropna(subset=['Medal']).groupby(['Year', 'Medal'])
    result = {}
    for (year, medal), group in grouped_data:
        if year not in result:
            result[year] = {'G':0, 'S':0, 'B':0}
        if medal == 'Gold':
            result[year]['G'] = len(group)
        elif medal == 'Silver':
            result[year]['S'] = len(group)
        elif medal == 'Bronze':
            result[year]['B'] = len(group)
    print(result)
