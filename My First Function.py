### Basic EDA Function ###
import numpy as np
import pandas as pd

def analyze(data):
    """A BASIC FUNCTION WITH ALL INITIAL PANDAS FUNCTION FOR BASIC EDA"""
    print('--------------------------------------------INITIAL ANALYSIS REPORT--------------------------------------------')
    data.columns = data.columns.str.strip().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('%', 'perc')
    display('DATA SHAPE')
    print('The number of rows (observations) is',data.shape[0],'\n''The number of columns (variables) is',data.shape[1])
    print('-----------------------------------------------')
    display('DATA INFO')
    display(data.info())
    print('---------------------------------------------------------------------------------------------------------------')
    display('DATA HEAD (First 15 records)', data.head(15))
    print('---------------------------------------------------------------------------------------------------------------')
    display('DATA TAIL (Last 15 records)', data.tail(15))
    for column in data.columns:
        if data[column].dtype == 'int':
            print('---------------------------------------------------------------------------------------------------------------')
            display('DATA DESCRIPTION (DISCRETE VARIABLES)', data.describe(include = 'int').T)
            break
    for column in data.columns:  
        if data[column].dtype == 'float':
            print('---------------------------------------------------------------------------------------------------------------')
            display('DATA DESCRIPTION (CONTINUOUS VARIABLES)', data.describe(include = 'float').T)
            break
    
    data_types = ['int', 'float' 'object']
    for column in data.columns:
        if data[column].dtype != 'int':
            if data[column].dtype != 'float':
                if data[column].dtype != 'object':
                    print('---------------------------------------------------------------------------------------------------------------')
                    display('DATA DESCRIPTION (OTHER VARIABLES)', data.describe(exclude = data_types).T)
        else:
            break
    print('---------------------------------------------------------------------------------------------------------------')
    display('DATA DESCRIPTION (CATEGORICAL VARIABLES)')
    print('---------------------------------------------------------------------------------------------------------------')         
    for column in data.columns:
        if data[column].dtype == 'object':
            print(column.upper(),': ',data[column].nunique())
            print(data[column].value_counts().sort_values(ascending=False))
            print('\n')
    print('---------------------------------------------------------------------------------------------------------------')        
    display('DATA NULLS COUNT', data.isnull().sum())
    print('---------------------------------------------------------------------------------------------------------------')
    display('DATA DUPLICATES COUNT', data.duplicated().sum())
    print('--------------------------------------------------END OF REPORT------------------------------------------------')
   
