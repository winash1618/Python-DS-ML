"""youngest_fellah
    """

import pandas as pd

def youngest_fellah(df, year):
    """Write a function youngest_fellah that takes two arguments:
        • a pandas.DataFrame which contains the dataset
        • an Olympic year.
        The function returns a dictionary containing the age of the youngest woman and man
        who took part in the Olympics on that year. The name of the dictionary's keys is up to
        you, but it must be self-explanatory

    Args:
        df (data.DataFrame): dataset
        year (int): an Olympic year
    """
    # data = {
    #     'name': ['Alice', 'Bob', 'Charlie'],
    #     'age': [25, 30, 35],
    #     'country': ['USA', 'Canada', 'Australia']
    # }
    
    # df = pd.DataFrame(data)
    
    # Select only the 'name' and 'age' columns where age is greater than 30
    # subset_df = df.loc[df['age'] > 25]
    # selected_df = subset_df.loc[subset_df['name'] == 'Bob']
    
    # Another way selected_df = df.loc[df.loc[df['age'] > 25]['name'] == 'Bob']
    
    # Display the selected columns
    # print(selected_df)
    # sel = df.loc[df['Year'] == year]
    # sel1 = sel.loc[sel['Sex'] == 'M']
    # sel2 = sel.loc[sel['Sex'] == 'F']
    # male_age = sel1.loc[sel1['Age'] == min(sel1['Age'])][['Age']].min()
    # female_age = sel2.loc[sel2['Age'] == min(sel2['Age'])][['Age']].min()
    # print({'m': male_age['Age'], 'f': female_age['Age']})
    # sel = df.loc[df['Age'] == min(df['Age'])]
    min_ages = df[df['Year'] == year].groupby('Sex')['Age'].min()
    print(min_ages.head())
    # print({'m': min_ages['M'], 'f': min_ages['F']})
    # selected_df = df.loc[df['Age'] == min(df['Age']) & (df['Year'] == year) & (df['Sex'] == 'M')]
    # print(selected_df)