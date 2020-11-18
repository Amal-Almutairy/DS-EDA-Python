# chickwts analysis

#%%
# libraries
import math 
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols


#%%
import matplotlib.pyplot as plt 
%matplotlib inline
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.base.model import Model

#%%
# import the data
chickwts = pd.read_csv('chickwts.csv')


#%%
## Read the dataset into a 
print(chickwts)

#%%
# type:
print(type(chickwts))

#%%
# Examine the data
chickwts.info()
chickwts.shape
chickwts.columns
chickwts.describe()


#%%
# explore first dataset rows
chickwts.head()


#%%
sns.boxplot(x='feed', y='weight', data=chickwts)

# %%
sns.catplot(x="feed", y="weight", data=chickwts)
# %%
sns.pointplot(x="feed", y="weight", data=chickwts, join=False)
# alternatively:
# sns.catplot(x="feed", y="weight", data=chickwts, kind="point")

## T-rest
# %%
# fit a linear model
# specify model
model = ols("weight ~ feed", chickwts)

#%%
# fit model
results = model.fit()
# %%
# extract coefficients
results.params.Intercept


# %%
# Explore model results
results.summary()

# %%
# ANOVA
# compute anova
aov_table = sm.stats.anova_lm(results, typ=2)

#%%
# explore anova results
aov_table

# %%
chickwts.groupby(['feed']).describe()


# %%
# Produces Pandas DataFrame
chickwts.groupby('feed')[['weight']].mean()


# %%
chickwts.groupby(['feed']).agg({'weight':['mean','std']})

