
#To categorize all the dtype: 'object' columns inplace in the dataframe df: 

df[df.select_dtypes(['object']).columns] = df.select_dtypes(['object']).apply(lambda x: x.astype('category'))