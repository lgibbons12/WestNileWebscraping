# WestNileWebscraping
This is a collection of webscraping scripts used to turn html data tables from this website: https://dph.illinois.gov/topics-services/diseases-and-conditions/west-nile-virus, and turn them into one pandas dataframe that is saved to excel


sel.py is a script that goes into webpages which have clickable links for each county, and aggregates the tables within each link into one full excel file

webscrape.py is a script that goes into the webpage and simply saves the table on the webpage to an excel file
