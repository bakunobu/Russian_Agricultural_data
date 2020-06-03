def add_line(data, data_frame=df):
       '''
       A simple adding function for the table 1.1 fod 2016 All-Russian
       Agricultural Census.
       pandas is required.
       Args:
       =====
       data: iterable
       a list or a tuple with data (14 columns) all must be filled with data
       (np.NaN - for all the missing values)
       
       data_frame: pandas DataFrame object
       Must be pre-created - the dataframe is being modified with the .append() method
       Returns:
       ========
       data_frame: pandas DataFrame object
       a modified data_frame
       '''
       
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
