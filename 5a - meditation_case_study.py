# The Meditation Case Study

#%%
import pandas as pd
import numpy as np


# %%
medi = pd.read_table("Expression.csv")

#%%
# medi
medi.columns

#%%
# Examples on getting tidy data
medi_clean = pd.melt(
    medi,
    id_vars=['Control_RIPK2_1'],
    var_name=['Control_RIPK2_2'],
    value_name='Meditation_RIPK2_1'
)
print(medi_clean) 


#%%
# Make a DataFrame
df = pd.DataFrame({
            'name': ["John Smith", "Jane Doe", "Mary Johnson"],
            'treatment_a': [None, 16, 3], 
            'treatment_b': [2, 11, 1]})
df

#%%
medi_clean.to_csv('tidy_data_example1-clean.csv')

# %%
# use melt to get tidy data
# The id variables stay the same before and after melting
# The measure variables will become a key:value pair 
df_melt = pd.melt(df, id_vars='name')
df_melt
# %%
df_melt_pivot = pd.pivot_table(df_melt,
                               index='name',
                               columns='variable',
                               values='value')

df_melt_pivot

df_melt_pivot.reset_index()                    


# %%
# Add an index column, but it's not necessary
# medi_index = medi.reset_index()
# medi_index


#%%
# If we had the index column:
medi_melt = pd.melt(medi_index, id_vars='index')

# If we don't have an index column, or ID variables: 
medi_melt = pd.melt(medi)
medi_melt

# This is "long" data, but *not* tidy! 


# %%
# To really be tidy:
# 1 obs per row
# 1 variable per column
# Here: 3 variables in the "variable" column: treatment, gene, time
# We need to split them up into three distinct columns!
# medi.unstack()

# this just gets treatments:
medi_melt['treatment'] = medi_melt['variable'].str.split('_').str.get(0)


#%%
# split up the three variables, call the .str attribute to get strings
medi_melt['treatment'], medi_melt['gene'], medi_melt['time'] = medi_melt['variable'].str.split('_').str

# %%
# Drop the variable column
medi_melt.drop('variable', axis=1)

# %%
