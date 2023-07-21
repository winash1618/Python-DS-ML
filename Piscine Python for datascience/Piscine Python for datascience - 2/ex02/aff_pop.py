from load_csv import load
import matplotlib.pyplot as plt

df = load("../population_total.csv")
# Replace 'Desired Country 1' and 'Desired Country 2' with the names of the countries you want to plot
desired_country1 = 'France'
desired_country2 = 'Germany'

# Filter the DataFrame to get the data for the first country
filtered_df1 = df[df['country'] == desired_country1]

# Get the years as the x-axis
years = df.columns[1:]

# Custom function to convert population values
def convert_population(pop_value):
    if pop_value.endswith('M'):
        return float(pop_value[:-1]) * 1000000
    elif pop_value.endswith('k'):
        return float(pop_value[:-1]) * 1000
    else:
        raise ValueError(f"Invalid population format: {pop_value}")

# Convert population data for the first country to numeric values
population1 = [convert_population(pop) for pop in filtered_df1.values[0][1:]]

# Filter the DataFrame to get the data for the second country
filtered_df2 = df[df['country'] == desired_country2]

# Convert population data for the second country to numeric values
population2 = [convert_population(pop) for pop in filtered_df2.values[0][1:]]

# Plot the population trends for both countries on the same plot
plt.plot(years, population1, label=desired_country1)
plt.plot(years, population2, label=desired_country2)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Projections')

# Set x-axis tick positions and labels for every 40 years
plt.xticks(years[::40])

# Set y-axis tick positions and labels for every 40 million
max_population = max(max(population1), max(population2))
yticks = [i * 40_000_000 for i in range((int(max_population) // 40_000_000) + 1)]
plt.yticks(yticks, [f'{i // 1_000_000}M' for i in yticks])

# Show the legend to differentiate between the two countries
plt.legend()

# Show the plot
plt.show()