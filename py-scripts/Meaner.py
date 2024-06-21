import pandas as pd
import numpy as np

class Meaner:
    def __init__(self, df):
        self.df = df
    
    def get_mean_mode(self, column):
        if self.df[column].dtype.kind in 'bifc':  # check if the column is numeric
            return self.df[column].mean()
        else:
            # For non-numeric columns, calculate the mode (most frequent value)
            mode_value = self.df[column].mode()[0]
            return mode_value