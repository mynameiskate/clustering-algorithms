from maxmin_clusterer import MaxMinClusterCreator
from k_clusterer import KClusterCreator
from plotter import Plotter

# Defining parameters
CLUSTERS = 6
OBSERVATIONS = 20000
MIN_VALUE = 0
MAX_VALUE = 100

# K-means clustering
analyzer = KClusterCreator(6, 20000, 0, 100)
res = analyzer.create_clusters()

# K-means Plotting
plotter = Plotter(analyzer.centers, res, analyzer.color_map)
plotter.set_title('K-means clustering')
plotter.plot()

# Maxmin clustering
maxmin_analyzer = MaxMinClusterCreator(20000, 0, 100)
res = maxmin_analyzer.create_clusters()

# Maxmin plotting
plotter = Plotter(maxmin_analyzer.centers, res, analyzer.color_map)
plotter.set_title('Maxmin clustering')
plotter.plot()

