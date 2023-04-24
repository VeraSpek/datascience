import pandas as pd
import numpy as np

def import_dataset(deaths_data, cases_data, UV_data):
    """Function that imports the 3 datasets with information about the deaths, cases and UV-UV_index
    per US state. Afterwards, data is ready to be processed into one dataset.
    Returns 3 dataframes containing the death, cases and UV dataset."""

    #Importing the mortality.csv file
    df_deaths = pd.read_csv(deaths_data, header = 1)
    df_deaths.rename(columns={"000": "Lower CI", "Lower CI": "Upper CI", "Upper CI": "Absolute_number"}, inplace = True) # renaming columns because they are not aligned with the data correctly
    del df_deaths[df_deaths.columns[-1]]
    print(df_deaths)

    # Importing the Incidence.csv file
    df_cases = pd.read_csv(cases_data, header = 1)
    df_cases.rename(columns={"000": "Lower CI", "Lower CI": "Upper CI", "Upper CI": "Absolute_number"}, inplace = True) #renaming columns because they are not aligned with the data correctly
    del df_cases[df_cases.columns[-1]] # removing last column because this is empty_knapsack

    # Importing the UV_index.csv file
    df_UV_index = pd.read_csv(UV_data)

    return df_deaths, df_cases, df_UV_index # returning 3 dataframes that can be merged together

def combining_datasets(deaths, cases, UV):
    """Function makes one dataframe containing all the columns needed for the regression model.
    Returns one datasset that can be used to make the regression model. """

if __name__ == '__main__':
    """ Main Function"""
    df_deaths, df_cases, df_UV_index = import_dataset('Mortality.csv', 'Incidence.csv', 'uv-county.csv')

    # Information on the unedited datasets
    # df_deaths.info()
    # df_cases.info()
    # df_UV_index.info()
