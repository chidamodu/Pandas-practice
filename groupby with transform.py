df['new_column_name'] = df.groupby('cn')['cn'].transform('count') #Groupby column 'cn' and the second 'cn' is what I count on. It returns the dataset with a new column added with count values in the name: 'new_column_name'