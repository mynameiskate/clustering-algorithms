import pandas as pd
import numpy as np
from math_helper import MathHelper


class ClusterCreator:
    color_map = {1: 'm', 2: 'c', 3: 'b', 4: 'y', 5: '#FA4411', 6: 'g'}

    def __init__(self, cluster_count, observation_count, min, max):
        self.cluster_count = cluster_count
        self.observation_count = observation_count
        self.observations = pd.DataFrame({
            'x': MathHelper.get_random_arr(min, max, observation_count),
            'y': MathHelper.get_random_arr(min, max, observation_count)
        })
        self.centers = MathHelper \
            .get_random_df_elements(self.observations, self.cluster_count)

    def _adjust_centers(self):
        for i in self.centers.keys():
            self.centers[i][0] = np\
                .mean(self.observations[self.observations['closest'] == i]['x'])
            self.centers[i][1] = np\
                .mean(self.observations[self.observations['closest'] == i]['y'])

    def set_color_map(self, color_map):
        self.color_map = color_map

    def clusterize(self):
        self.observations = MathHelper\
            .map_df_to_clusters(self.observations, self.centers, self.color_map)
        self._adjust_centers()
        self.finalize_centers()

        return self.observations

    def finalize_centers(self):
        while True:
            closest_centers = self.observations['closest'].copy(deep=True)
            self.observations = MathHelper \
                .map_df_to_clusters(self.observations, self.centers, self.color_map)
            self._adjust_centers()
            if closest_centers.equals(self.observations['closest']):
                return
