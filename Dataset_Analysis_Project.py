
"""


@author: Ho Wing Wong (Louie)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sci

#http://data.worldbank.org/ <--- The data source

data = pd.read_csv('2015_dataset.csv')
Dict = {'GDP':'2015 GDP per capita (current US$)', \
        'Internet':'2015 Internet users (per 100 people)',\
        'Water':'2015 Improved water source (% of population with access)'} # Dictionary that allows me  type less

#Graphs 1 & 2

graph1 = sns.lmplot(data = data, x = Dict['GDP'], y = Dict['Water'],fit_reg = False)

graph2 = sns.lmplot(data = data, x = Dict['GDP'], y = Dict['Internet'],fit_reg = False)


           
#Array syntax
GDP = np.array(data[Dict['GDP']]) #Create an array from the DataFrame-GDP per capita
data[Dict['GDP']].describe()
Group = np.array(GDP,dtype = 'str') #Create a same size array with GDP, and the following is to group them in to different group
Group[np.where(GDP < 1579.024590)] = 'GDP per capita <25%'
Group[np.where(GDP >= 1579.024590)] = 'GDP per capita >=25% and <50%'
Group[np.where(GDP >= 5716.071633)] = 'GDP per capita >=50% and < 75%'
Group[np.where(GDP >= 13780.925710)] = 'GDP per capita >=75%'
data['GDP per capita Group'] = Group #Create a new column on the dataframe 

#Graphs 3
graph3 = sns.lmplot(data = data, x = Dict['Water'], y = Dict['Internet'],\
                    fit_reg = False, hue = 'GDP per capita Group')

#non-graphical analysis
data[Dict['GDP']].describe() #Mean, std, min, 25%, 50%, 75% and max of GDP data
data[Dict['Water']].describe() #Mean, std, min, 25%, 50%, 75% and max of Water source data
data[Dict['Internet']].describe() #Mean, std, min, 25%, 50%, 75% and max of internet users data
sci.corrcoef(data[Dict['GDP']],data[Dict['Water']])[0][1] #correlation coefficient of GDP vs Water source
sci.corrcoef(data[Dict['GDP']],data[Dict['Internet']])[0][1] #correlation coefficient of GDP vs Internet users
      
fil1 = data[(data[Dict['Water']]>40) & (data[Dict['Water']]<50)& (data[Dict['Internet']]>20)].CountryName
# Fil1 is the filter of the country that has high GDP per capita, but low internet user and improved water source
#Equatorial Guinea <--- the country name
#http://www.bbc.com/news/world-africa-13317174 <---- Information of the country
plt.show()

#Paragraph discussion
'''
Graph1 shows 2015 Improved water source (% of population with access) vs 2015 GDP per capita (current US$)
We can see that the basically most of the countries, even those with the low GDP per capita have a high Imporved water source,
Becasue water is human basic needs. And Graph2 shows Internet':'2015 Internet users (per 100 people) vs 2015 GDP per capita (current US$)
We can see that They are kind of similar, but Graph2 is less extreme. We can indicated that internet is becoming a basic human needs,
which it is important that human have the ability to access internet. 
Graph3 shows 2015 Improved water source (% of population with access) vs 2015 Internet users (per 100 people) with Grouping of 
GDP per capita. It shows us the higher the GDP per capita, the higher the internet user and imporved water source. Something interesting is
that, there is a country that has high GDP per capita, but low internet user and improved water source (Check fil1), which is Equatorial Guinea
it is a country in Africa, happens to have lots of natural resources- oil, but the government is corrupted. The profit gained from
the oil goes to the government instead of the citizen. 

'''

