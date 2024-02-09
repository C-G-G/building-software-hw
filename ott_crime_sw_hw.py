%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd 


# https://merely-useful.tech/py-rse/config.html


ott_hate_crime = pd.read_csv('./Hate_and_Bias_Motivated_Crime.csv')

ott_hate_crime.head()

# text columns (most common values (top), unique values)
ott_hate_crime.describe(include=['O'])

## 5. Unique values of the primary hate crime motivation column
ott_hate_crime['HATE_CRIME_TYPE'].unique()

ott_hate_crime['PRIMARY_HATE_CRIME_MOTIVATION'].unique()

## 6. Counts of the Primary Hate Crime Motivation column values
ott_hate_crime['PRIMARY_HATE_CRIME_MOTIVATION'].value_counts()

## 7. Convert UCR_Code data type from int to str
ott_hate_crime['UCR_CODE'].dtype
ott_hate_crime['UCR_CODE'] = ott_hate_crime['UCR_CODE'].astype('string')
ott_hate_crime['UCR_CODE'].dtype


# 1. Use groupby() to split data into groups based on one of the columns
crime_type_groups = ott_hate_crime.groupby(['HATE_CRIME_TYPE'])
crime_type_groups.size().sort_values(ascending=[False])

motivation_groups = ott_hate_crime.groupby(['PRIMARY_HATE_CRIME_MOTIVATION'])
motivation_groups.size().sort_values(ascending=[False])

neighbourhood_groups = ott_hate_crime.groupby(['OTTAWA_NEIGHBOURHOOD'])
neighbourhood_groups.size().sort_values(ascending=[False])

# 2. Summary table using agg() on ...
ott_hate_crime_summary = (ott_hate_crime.groupby('Year')
                          .agg(neighbourhood_count=('OTTAWA_NEIGHBOURHOOD', 'count'),
                               crime_type_count=('HATE_CRIME_TYPE', 'count'),
                               crime_motivation_count=('PRIMARY_HATE_CRIME_MOTIVATION', 'count')))

ott_hate_crime_summary



plt.scatter(ott_hate_crime['Year'],
            ott_hate_crime['HATE_CRIME_TYPE'],
            marker='s',  # square marker
            facecolor='#fb1',
            edgecolor='k') # black

plt.savefig('ott_hate_crime.png')