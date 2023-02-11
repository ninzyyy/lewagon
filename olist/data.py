import os
import pandas as pd


class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities

        csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data/csv")
        file_names = os.listdir(csv_path)
        file_names.remove(".keep")

        key_names = file_names
        key_names = [file.replace(".csv", "").replace("_dataset","").replace("olist_","") for file in key_names]

        dataframes = []
        for file in file_names:
            df = pd.read_csv(os.path.join(csv_path, file))
            dataframes.append(df)
            print(df)

        data = dict(zip(key_names, dataframes))
        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
