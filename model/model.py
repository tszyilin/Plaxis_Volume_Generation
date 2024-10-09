import pandas as pd
import numpy as np

class PlaxisModel:
    def __init__(self):
        self.valid_rows_dict = {}
        self.error_code_dict = {
            1: 'Null Name',
            2: 'Shape is not C or R',
            3: 'Centroid_X is not a number',
            4: 'Centroid_Y is not a number',
            5: 'Centroid_Z is not a number',
            6: 'Dim_X is not a number',
            7: 'Dim_Y is not a number',
            8: 'Radius is not a number',
            9: 'Length is not a number',
            10: 'No radius for circle',
            11: 'No X dimension for rectangular',
            12: 'No Y dimension for rectangular',
            13: 'No Length',
            14: 'Radius is incorrect',
            15: 'Dim_X is incorrect',
            16: 'Dim_Y is incorrect'
        }

    def plaxis_volume_generation(self, file_name):
        df = pd.read_excel(file_name)

        for i in range(len(df)):
            if df['Shape'][i] == 'C':
                df.at[i, 'Dim_X'] = np.nan
                df.at[i, 'Dim_Y'] = np.nan
            elif df['Shape'][i] == 'R':
                df.at[i, 'Radius'] = np.nan

            error_code_list = []
            error_conditions = {
                1: pd.isna(df['Name'][i]),
                2: df['Shape'][i] not in ["C", "R"],
                3: isinstance(df['Centroid_X'][i], str),
                4: isinstance(df['Centroid_Y'][i], str),
                5: isinstance(df['Centroid_Z'][i], str),
                6: isinstance(df['Dim_X'][i], str),
                7: isinstance(df['Dim_Y'][i], str),
                8: isinstance(df['Radius'][i], str),
                9: isinstance(df['Length'][i], str),
                10: df['Shape'][i] == 'C' and pd.isna(df['Radius'][i]),
                11: df['Shape'][i] == 'R' and pd.isna(df['Dim_X'][i]),
                12: df['Shape'][i] == 'R' and pd.isna(df['Dim_Y'][i]),
                13: pd.isna(df['Length'][i]),
                14: df['Shape'][i] == 'C' and df['Radius'][i] <= 0,
                15: df['Shape'][i] == 'R' and df['Dim_X'][i] <= 0,
                16: df['Shape'][i] == 'R' and df['Dim_Y'][i] <= 0
            }

            for code, condition in error_conditions.items():
                    if condition:
                        error_code_list.append(code)

            if len(error_code_list) != 0:
                error_messages = [
                    self.error_code_dict[code] for code in error_code_list
                ]
                yield i + 1, error_messages
            else:
                row_data = {
                    'Shape': df['Shape'][i],
                    'Centroid_X': df['Centroid_X'][i],
                    'Centroid_Y': df['Centroid_Y'][i],
                    'Centroid_Z': df['Centroid_Z'][i],
                    'Dim_X': df['Dim_X'][i],
                    'Dim_Y': df['Dim_Y'][i],
                    'Radius': df['Radius'][i],
                    'Length': df['Length'][i]
                }
                self.valid_rows_dict[df['Name'][i]] = row_data

        return self.valid_rows_dict
