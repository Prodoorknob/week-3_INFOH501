import seaborn as sns
import pandas as pd
import numpy as np

# update/add code below ...
# exercise 3 Part 1 and Part 2
# Recursive functions


def fibonacci(n):

    """A function that returns the nth number in the Fibonacci sequence"""

    if n<0: #Case to catch negative numbers
        return ("Please enter numbers greater then 0")
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2) #recursion to calculate the nth number in sequence


def to_binary(n):

    """A function that returns the binary form of the integer n"""

    if n<0:
        return "-"+ to_binary(-n) # case to handle negative integers
    if n<2:
        return str(n)
    return to_binary(n//2)+ str(n%2) # recursion to convert the integer to binary


#Test case for above functions
print(fibonacci(0))
print(fibonacci(12))
print(to_binary(34))
print(to_binary(0))
print(to_binary(2))

# exercise 3 Part 3 
# pandas



url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)

df_bellevue['gender']=df_bellevue['gender'].replace('?', np.nan )


def task_1():

    """Returns a list of columns in ascending order of their total null counts"""

    counts={c:df_bellevue[c].isna().sum() for c in df_bellevue.columns} #finding the null count in each column and creating a dictionary contaning the null counts and corresponding columns
    return sorted(counts, key=lambda c: (counts[c], c))                 #sorting the dictionary based on null counts:counts[c](value of dict) and column names:c(key of dict) to deal with cases where multiple columns have 0 null values


df_bellevue['Year']=pd.to_datetime(df_bellevue['date_in']).dt.year


def task_2():

    """Returns a two-column DataFrame: year and total_admissions"""

    df_new=df_bellevue[['Year', 'disease']]
    df_grouped=df_new.groupby('Year').agg(total_admissions= ('disease','size'))
    return df_grouped


def task_3():

    """Returns a series of average age with gender as index"""

    return df_bellevue.dropna().groupby('gender')['age'].mean().sort_index()


def task_4():

    """Returns a list of the 5 most common professions in order of prevalence"""

    return df_bellevue.dropna().groupby('profession')['profession'].count().sort_values(ascending=False).index.to_list()
