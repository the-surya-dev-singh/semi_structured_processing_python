import pandas as pd
import numpy as np
from pandas import json_normalize
from matplotlib import pyplot as plt
import json

movies=[{'director': 'Woody Allen',
  'producer': 'Letty Aronson',
  'features': {'title': 'Magic in the Moonlight', 'year': 2014}},
 {'director': 'Niki Caro',
  'producer': 'Jason Reed',
  'features': {'title': 'Mulan', 'year': 2020}}]
movies2=[{'director': 'Woody Allen',
  'producer': 'Letty Aronson',
  'features': [{'title': 'Magic in the Moonlight', 'year': 2014},
   {'title': 'Vicky Cristina Barcelona', 'year': 2008},
   {'title': 'Midnight in Paris', 'year': 2011}]},
 {'director': 'Niki Caro',
  'producer': 'Jason Reed',
  'features': [{'title': 'Mulan', 'year': 2020}]}]
print(movies)
movies_norm=json_normalize(movies)
print(movies_norm)
movies_norm2=json_normalize(movies2,record_path='features',meta=['producer','director'])
print(movies_norm2)


# Replace  with the path to your JSON file
json_file_path = 'c:/Users/User/Desktop/python_test/test.json'

# Read the JSON data into a pandas DataFrame
df = pd.read_json(json_file_path)

# Set display options to print all columns and disable truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Extract the 'person' data as a separate DataFrame
person=json_normalize(df['person']).drop(columns=['education'],axis=1)#.explode('hobbies')

hobbies=person[['name','hobbies']]
hobbies=hobbies.explode('hobbies')
person.drop(columns='hobbies',inplace=True)
'''
person=person.explode('hobbies')
hobbies=person[['name','hobbies']]
'''

education=json_normalize(df['person'],record_path='education',meta=['name'])
project=json_normalize(df['projects'][0])
project['name']=person['name'][0]
company=df[['company','position','years_of_experience']]
person[['company','position','years_of_experience']]=company #adding columns for the person's company profile
print(person)
print(hobbies)
print(education)
print(company)
print(project)


#person_df=person_df.explode('hobbies')
