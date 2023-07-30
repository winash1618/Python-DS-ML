from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load data from a CSV file, filter data for a desired country,
    and plot the life expectancy trend.

    Note: Replace 'Desired Country' with the name of the country you
    want to plot.
    """
    df = load("../life_expectancy_years.csv")

    # Replace 'Desired Country' with the name of the country you want to plot
    desired_country = 'France'
    filtered_df = df[df['country'] == desired_country]

    # Get the years as the x-axis
    years = df.columns[1:]

    # Get the life expectancy data for the desired country
    life_expectancy_data = filtered_df.iloc[:, 1:].values.flatten()

    # Plot the life expectancy trend for the desired country
    plt.plot(years, life_expectancy_data)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.title(f'Life Expectancy Over Time for {desired_country}')

    # Set x-axis tick positions and labels for every 40 years
    plt.xticks(years[::40])

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
