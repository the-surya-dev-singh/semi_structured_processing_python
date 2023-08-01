import pandas as pd
import numpy as np
from pandas import json_normalize
from matplotlib import pyplot as plt
import json

# Replace  with the path to your JSON file
json_file_path = 'c:/Users/User/Desktop/python_test/test2.json'

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
company=df[['company','position','years_of_experience']]
person[['company','position','years_of_experience']]=company #adding columns for the person's company profile


print(person)
print(hobbies)
print(education)
print(company)
for x in range(len(df)):
    project=json_normalize(df['projects'][x])
    project['name']=person['name'][x]
    print(project)
