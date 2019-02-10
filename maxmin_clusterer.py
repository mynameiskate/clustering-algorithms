import pandas as pd
from math_helper import MathHelper


class MaxMinClusterCreator:
    color_map = {1: 'm', 2: 'c', 3: 'b', 4: 'y', 5: '#FA4411', 6: 'g',
                 7: '#7dce94', 8: '#bd8c7d', 9: '#fa625f', 10: '#00303F',
                 11: '#FF5A09', 12: '#201d3a'}

    def __init__(self, observation_count, min, max):
        self.observation_count = observation_count
        self.observations = pd.DataFrame({
            'x': MathHelper.get_random_arr(min, max, observation_count),
            'y': MathHelper.get_random_arr(min, max, observation_count)
        })
        self.centers = MathHelper \
            .get_random_df_elements(self.observations, element_count=1)

    def set_color_map(self, color_map):
        self.color_map = color_map

    def create_clusters(self):
        self.observations = MathHelper\
            .map_df_to_clusters(self.observations, self.centers,
                                self.color_map, calc_center_dist=True)
        next_center = MathHelper\
            .get_farthest_element(self.observations, 'distance_from_1')
        self.centers.update({2: [next_center['x'], next_center['y']]})
        self.finalize()

        return self.observations

    def finalize(self):
        while True:
            self.observations = MathHelper \
                .map_df_to_clusters(self.observations, self.centers,
                                    self.color_map, calc_center_dist=True)
            next_center = MathHelper\
                .get_farthest_element(self.observations, 'distance_from_center')
            average_center_dist = MathHelper.get_average_distance(self.centers)
            if next_center['distance_from_center'] > average_center_dist:
                self.centers\
                    .update({len(self.centers.keys()) + 1: [next_center['x'], next_center['y']]})
            else:
                break
