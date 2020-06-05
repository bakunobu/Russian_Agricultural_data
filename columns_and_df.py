import pandas as pd
import numpy as np

columns = ['indicator',
           'all_2006',
           'all_2016',
           'companies_2006',
           'companies_2016',
           'farmers_and_IE_2006',
           'farmers_and_IE_2016', 
           'farmers_2006',
           'farmers_2016',
           'IE_2006',
           'IE_2016',
           'personal_2006',
           'personal_2016',
           'non_profit_2006',
           'non_profit_2016']

df = pd.DataFrame(columns=columns)

line_1 = pd.DataFrame({'indicator': ['число хоз-в всего (тыс)'],
           'all_2006': [np.NaN],
           'all_2016': [np.NaN],
           'companies_2006': [59.2],
           'companies_2016': [36.0],
           'farmers_and_IE_2006': [285.1],
           'farmers_and_IE_2016': [174.8], 
           'farmers_2006': [253.1],
           'farmers_2016': [136.7],
           'IE_2006': [32.0],
           'IE_2016': [38.0],
           'personal_2006': [22799.4],
           'personal_2016': [23496.9],
           'non_profit_2006': [80.3],
           'non_profit_2016': [75.9]})

df= df.append(line_1, ignore_index=True)

line_2 = pd.DataFrame({'indicator': ['осуществояющих хоз. деят. в перв. полугодии (тыс)'],
           'all_2006': [np.NaN],
           'all_2016': [np.NaN],
           'companies_2006': [40.6],
           'companies_2016': [27.5],
           'farmers_and_IE_2006': [147.5],
           'farmers_and_IE_2016': [115.6], 
           'farmers_2006': [126.2],
           'farmers_2016': [90.2],
           'IE_2006': [21.3],
           'IE_2016': [25.4],
           'personal_2006': [20219.2],
           'personal_2016': [18752.4],
           'non_profit_2006': [74.5],
           'non_profit_2016': [67.6]})
df = df.append(line_2, ignore_index=True)

def add_line(data, data_frame=df):
    line = pd.DataFrame({'indicator': [data[0]],
           'all_2006': [data[1]],
           'all_2016': [data[2]],
           'companies_2006': [data[3]],
           'companies_2016': [data[4]],
           'farmers_and_IE_2006': [data[5]],
           'farmers_and_IE_2016': [data[6]], 
           'farmers_2006': [data[7]],
           'farmers_2016': [data[8]],
           'IE_2006': [data[9]],
           'IE_2016': [data[10]],
           'personal_2006': [data[11]],
           'personal_2016': [data[12]],
           'non_profit_2006': [data[13]],
           'non_profit_2016': [data[14]]})
    data_frame = data_frame.append(line, ignore_index=True)
    return(data_frame)


test_data = ('осуществояющих хоз. деят. в перв. полугодии (%)',
        np.NaN, np.NaN, 68.6, 76.3, 51.7, 66.1, 49.9,
        65.9, 66.5, 66.9, 88.7, 79.8, 92.7, 89.0)

df = add_line(test_data, df)
df.head()