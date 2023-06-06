#imports
import requests
import pandas as pd


#get the url from the user
URL = input('Copy the url here: ')




#grab the page and convert to text
page = requests.get(URL)
df_list = pd.read_html(page.text)

#take the table that has the info we want
df = df_list[2]


#make the columns
df.columns = df.iloc[0]


#convert the data from strings to integers
for i in range(len(df.columns)):
    if i == 0:
        continue

    df.iloc[1:, i] = pd.to_numeric(df.iloc[1:, i])

#save it to an excel file
df.to_excel("output.xlsx", index=False)


