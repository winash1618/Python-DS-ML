from load_csv import load
import matplotlib.pyplot as plt


def convert_population(pop_value):
    """
    Convert population values from string to numeric format.

    Args:
        pop_value (str): The population value as a string
        (e.g., '100k', '10M').

    Returns:
        float: The population value as a numeric float.

    Raises:
        ValueError: If the population format is invalid.
    """
    if pop_value.endswith('M'):
        return float(pop_value[:-1]) * 1000000
    elif pop_value.endswith('k'):
        return float(pop_value[:-1]) * 1000
    else:
        raise ValueError(f"Invalid population format: {pop_value}")


def main():
    """
    Load data from a CSV file, filter data for desired countries,
    and plot the population trends.

    Note: Replace 'Desired Country 1' and 'Desired Country 2'
    with the names of the countries you want to plot.
    """
    df = load("../population_total.csv")
    desired_country1 = 'France'
    desired_country2 = 'Germany'

    filtered_df1 = df[df['country'] == desired_country1]

    years = df.columns[1:]

    population1 = [convert_population(pop) for pop in
                   filtered_df1.values[0][1:]]

    filtered_df2 = df[df['country'] == desired_country2]

    population2 = [convert_population(pop) for pop in
                   filtered_df2.values[0][1:]]

    plt.plot(years, population1, label=desired_country1)
    plt.plot(years, population2, label=desired_country2)

    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')

    plt.xticks(years[::40])

    max_population = max(max(population1), max(population2))
    yticks = [i * 40_000_000 for i in
              range((int(max_population) // 40_000_000) + 1)]
    plt.yticks(yticks, [f'{i // 1_000_000}M' for i in yticks])

    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
