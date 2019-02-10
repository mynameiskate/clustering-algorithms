import random
import numpy as np
import pandas as pd


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
    def get_average_distance(elements):
        sum = 0
        el_count = len(elements.keys())

        for i in range(1, el_count):
            for k in range(i + 1, el_count + 1):
                sum += np.sqrt(
                    (elements[i][0] - elements[k][0]) ** 2
                    + (elements[i][1] - elements[k][1]) ** 2
                )

        return (sum / (el_count * (el_count - 1)))\
            if (el_count > 0)\
            else 0

    @staticmethod
    def calc_df_dist(df, dest_el):
        return np.sqrt(
                    (df['x'] - dest_el[0]) ** 2
                    + (df['y'] - dest_el[1]) ** 2
                )

    @staticmethod
    def get_farthest_element(df, label):
        return df.loc[df[label].idxmax(axis=1)]

    @staticmethod
    def calc_dist_to_centers(df):
        closest_centers = []
        for index, row in df.iterrows():
            closest_centers.append(row[row['closest']])

        return pd.Series(closest_centers)

    @staticmethod
    def map_df_to_clusters(df, centers, color_map, calc_center_dist=False):
        for i in centers.keys():
            df['distance_from_{}'.format(i)] = (
                MathHelper.calc_df_dist(df, centers[i])
            )

        centroid_distance_cols = ['distance_from_{}'.format(i) for i in centers.keys()]
        df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)

        if calc_center_dist:
            df['distance_from_center'] = MathHelper.calc_dist_to_centers(df)

        df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
        df['color'] = df['closest'].map(lambda x: color_map[x])

        return df
