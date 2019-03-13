'''
Created on 2019. 3. 12.

@author: Kangwoolim
'''

# Import the standard Python Scientific Libraries
import numpy as np
import warnings
import pandas as pd
import seaborn as sns
from scipy import stats
import warnings
import matplotlib.pyplot as plt

# Suppress Deprecation and Incorrect Usage Warnings
warnings.filterwarnings('ignore')


question = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\data\\schema.csv')
print(question.shape)

print(question.tail(10))

# MultipleChoiceQuestions

mcq = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\data\\multipleChoiceResponses.csv',
                  encoding="ISO-8859-1",low_memory=False)

print(mcq.shape)

print(mcq.head(10))

# nan data visualization - missingno
import missingno as msno
plt.show(msno.matrix(mcq, figsize=(12,5)))


# SurveyStatics
# 1. Gender

print(sns.countplot(y='GenderSelect', data = mcq))
# sns.countplot("column", "data = using data)

# 2. Country
con_df = pd.DataFrame(mcq['Country'].value_counts())
print(con_df)
