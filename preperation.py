import pandas as pd
import numpy as np

def import_dataset(deaths_data, cases_data, UV_data):
    """Function that imports the 3 datasets with information about the deaths, cases and UV-UV_index
    per US state. Afterwards, data is ready to be processed into one dataset.
    Returns 3 dataframes containing the death, cases and UV dataset."""

    #Importing the mortality.csv file
    df_deaths = pd.read_csv(deaths_data, header = 1)
    df_deaths.drop(df_deaths.columns[[1, 2, 3, 4, 6]], axis = 1, inplace = True)
    df_deaths.rename(columns={"Upper CI": "Melanoma_Deaths"}, inplace = True)
    df_deaths.sort_values('Area', inplace = True) #returns dataframe with two columns
    print(df_deaths.iloc[10:15,0])

    # Importing the Incidence.csv file
    df_cases = pd.read_csv(cases_data, header = 1)
    df_cases.drop(df_cases.columns[[1, 2, 3, 4, 6]], axis = 1, inplace = True)
    df_cases.rename(columns={"Upper CI": "Melanoma_Incidence"}, inplace = True)
    df_cases.sort_values('Area', inplace = True) #returns dataframe with two columns

    # Importing the UV_index.csv file,
    df_UV_index = pd.read_csv(UV_data)
    df_UV_index.drop(df_UV_index.columns[[1, 2, 3]], axis = 1, inplace = True)
    df_UV_index.rename(columns={"UV_ Wh/m_": "UV_Index", "STATENAME": "Area"}, inplace = True)
    mean_per_state = df_UV_index.groupby(['Area']).mean() #returns dataframe with two columns

    return df_deaths, df_cases, mean_per_state # dataframes are ready to be merged together

def combining_datasets(deaths, cases, UV):
    """Function makes one dataframe containing all the columns needed for the regression model.
    Returns one datasset that can be used to make the regression model. """

    result = pd.merge(pd.merge(deaths, cases, on= 'Area'), UV, on= 'Area')
    print(result)

    return result

if __name__ == '__main__':
    """ Main Function"""
    df_deaths, df_cases, df_UV_index = import_dataset('Mortality.csv', 'Incidence.csv', 'uv-county.csv')
    combined_df = combining_datasets(df_deaths, df_cases, df_UV_index)

    # combining_datasets(df_deaths, df_cases, df_UV_index)
