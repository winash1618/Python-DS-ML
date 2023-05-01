"""
ProportionBySport
The goal of this exercise is to create a function displaying the proportion of participants
who played a given sport, among the participants of a given genders.
"""


def proportion_by_sport(df, year, sport, gender):
    """Write a function proportion_by_sport that takes four arguments.
    The function returns a float corresponding to the proportion (percentage)
    of participants who played the given sport among the participants of the given gender.
    The function answers questions like the following : "What was the percentage of
    female basketball players among all the female participants of the 2016 Olympics?"

    Args:
        df (panda.DataFrame): a pandas.DataFrame of the dataset,
        year (int): an olympic year,
        sport (string): a sport
        gender (string): a gender
    """
    # proportion = df[df['Year'] == year]
    # proportion = proportion[proportion['Sex'] == gender]
    # proportion = proportion.drop_duplicates(subset=['Name'])
    # total_players = proportion.shape[0]
    # proportion = proportion[proportion['Sport'] == sport]
    # sport_players = proportion.shape[0]
    # print(sport_players / total_players)
    proportion = df[(df['Year'] == year) & (df['Sex'] == gender)].drop_duplicates(subset=['Name'])
    total_players = proportion.shape[0]
    sport_players = proportion[proportion['Sport'] == sport].shape[0]
    print(sport_players / total_players)
