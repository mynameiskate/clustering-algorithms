import matplotlib.pyplot as plt


class Plotter:
    min_value = 0
    max_value = 100
    title = 'Clusters:'

    def __init__(self, centers, observations, color_map):
        self.centers = centers
        self.observations = observations
        self.color_map = color_map

    def set_size(self, min, max):
        self.min_value = min
        self.max_value = max

    def set_title(self, title):
        self.title = title

    def plot_titles(self):
        fig = plt.figure(figsize=(5, 5))
        plt.title(f"Clusters: {len(self.centers.keys())}\n"
                  f" Elements: {len(self.observations.keys())}")
        fig.canvas.set_window_title(self.title)

    def plot(self):
        self.plot_titles()
        plt.scatter(self.observations['x'], self.observations['y'],
                    color=self.observations['color'], alpha=0.5, edgecolor='k')
        for i in self.centers.keys():
            plt.scatter(*self.centers[i], color='#F0FFF0')

        plt.xlim(self.min_value, self.max_value)
        plt.ylim(self.min_value, self.max_value)
        plt.show()
