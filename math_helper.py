
import random
import numpy as np


class MathHelper:

    @staticmethod
    def get_random_arr(min_val, max_val, num):
        return [random.randrange(min_val, max_val) for _ in range(num)]

    @staticmethod
    def get_random_df_elements(df, element_count):
        return {
            i + 1: df.values[np.random.randint(0, len(df))]
            for i in range(element_count)
        }

    @staticmethod
    def map_df_to_clusters(df, centers, color_map):
        for i in centers.keys():
            df['distance_from_{}'.format(i)] = (
                np.sqrt(
                    (df['x'] - centers[i][0]) ** 2
                    + (df['y'] - centers[i][1]) ** 2
                )
            )

        centroid_distance_cols = ['distance_from_{}'.format(i) for i in centers.keys()]
        df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
        df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
        df['color'] = df['closest'].map(lambda x: color_map[x])

        return df
