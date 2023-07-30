from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load data from two CSV files, extract data for a specific year,
    and plot a scatter plot.

    Note: The code assumes that the CSV files contain
    columns for each year (e.g., '1900', '1910', ...).

    Example:
    - '../life_expectancy_years.csv' should have columns
    'country', '1900', '1910', etc.
    - '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
    should have columns 'country', '1900', '1910', etc.
    """
    df1 = load("../life_expectancy_years.csv")
    df2 = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    life_expectancy = df1['1900'].values
    gdp_per_capita = df2['1900'].values

    plt.scatter(gdp_per_capita, life_expectancy)
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')

    # Set the x-axis scaling to be logarithmic
    plt.xscale('log')

    # Set the x-axis tick positions and labels
    x_tick_positions = [300, 1000, 10000]
    x_tick_labels = ['300', '1K', '10K']
    plt.xticks(x_tick_positions, x_tick_labels)

    plt.show()


if __name__ == "__main__":
    main()
