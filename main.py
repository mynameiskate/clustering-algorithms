import matplotlib.pyplot as plt
from clusterer import ClusterCreator
from kplotter import Plotter

# Defining parameters
CLUSTERS = 6
OBSERVATIONS = 20000
MIN_VALUE = 0
MAX_VALUE = 100

# Getting things done
analyzer = ClusterCreator(6, 20000, 0, 100)
res = analyzer.clusterize()

# Plotting
plotter = Plotter(analyzer.centers, res, analyzer.color_map)
plotter.plot()
