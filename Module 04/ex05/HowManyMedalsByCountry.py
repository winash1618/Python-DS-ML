"""
The goal of this exercise is to write a function that returns a dictionary of dictionaries
giving the number and type of medal for each competition where the country delegation
earned medals.
"""

import pandas as pd

def how_many_medals_by_country(df, name):
    """
    Write a function how_many_medals_by_country that takes two arguments:
    • a pandas.DataFrame which contains the dataset
    • a country name.
    The function returns a dictionary of dictionaries giving the number and type of medal
    for each competition where the country delegation earned medals. The keys of the main
    dictionary are the Olympic games' years. In each year's dictionary, the key are 'G', 'S',
    'B' corresponding to the type of medals won.
    Duplicated medals per team games should be handled and not counted twice. Hint:
    You may find this list to be of some use.

    Args:
        df (_type_): _description_
        name (_type_): _description_
    """
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badminton', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Volleyball', 'Synchronized Swimming', 'Basebal', 'Rugby', 'Lacrosse', 'Polo']
    df = df[df['Team'] == name].dropna(subset=['Medal'])
    print(df.shape)
    for elem in team_sports:
        copy_data =  df[df['Sport'] == elem].drop_duplicates(subset=['Sport'])
        # print(df.shape, copy_data, "-----")
        df = df[df['Sport'] != elem]
        # print(df.shape, elem)
        df = df.append(copy_data)
    # grouped_data = df[df['Team'] == name].dropna(subset=['Medal']).groupby(['Year', 'Medal'])
    # data = data[~data['Team'].isin(team_sports)]
    grouped_data = df.dropna(subset=['Medal']).groupby(['Year', 'Medal'])
    # print(df)
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