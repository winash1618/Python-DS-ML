"""
test
"""
from FileLoader import FileLoader
from MyPlotLib import MyPlotLib
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
print(data.head())

feature_names = []
# Create an instance of the MyPlotLib class
mpl = MyPlotLib()

# Test the histogram() method
mpl.histogram(data, ['Age', 'Height'])

# Test the density() method
mpl.density(data, ['Weight', 'Age'])

# Test the pair_plot() method
mpl.pair_plot(data, ['Height', 'Weight', 'Age'])

# Test the box_plot() method
mpl.box_plot(data, ['Height', 'Weight'])
