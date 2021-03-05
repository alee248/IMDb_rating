import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use("seaborn-pastel")
import os

for dirname, _, filenames in os.walk('/Users/apple/Desktop/Data Science/IMBd EDA'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

df_rating = pd.read_csv("title.ratings.tsv.gz.tsv",
                        sep="\t", low_memory=False, na_values=["\\N","nan"])
df_rating.head()
df_rating.info() # more than 1.1M movie rating rows
df_rating.describe() # mean rating=6.88, smaller than the median
# average rating distribution shows a negatively skewed distribution where
# the median is greater than the mean. Vote counts cluster around smaller
# values with the standard deviation of 1.41 points.

ratings = dict(mean=df_rating.averageRating.mean(), median=df_rating.averageRating.median())
votes = dict(mean=df_rating.numVotes.mean(), median=df_rating.numVotes.median())

plt.figure(figsize=(15,5))
plt.subplot(1,2,1)  # create a plot with two plots on the x axis, start with the 1st one
axis1 = sns.distplot(df_rating.averageRating, kde_kws=dict(bw=0.2))
axis1.axvline(x=ratings['mean'], c=sns.color_palette('Set2')[1], label="mean={round(ratings['mean'],2)}")
axis1.axvline(x=ratings['median'], c=sns.color_palette('Set2')[2], label="median={round(ratings['median'],2)}")
plt.legend()
plt.subplot(1,2,2)
axis2 = sns.distplot(df_rating.numVotes, kde_kws=dict(bw=0.2))
axis2.axvline(x=votes['mean'], c=sns.color_palette('Set2')[1], label="mean={round(votes['mean'],2)}")
axis2.axvline(x=votes['median'], c=sns.color_palette('Set2')[2], label="median={round(votes['median'],2)}")
plt.legend()
plt.tight_layout()
plt.show()

buckets = 20
plt.figure(figsize=(15,6))
bins = pd.qcut(df_rating.numVotes,buckets,duplicates="drop").value_counts()
sns.barplot(x=bins.values,y=bins.index,orient="h")
plt.show()

