from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

#all the imports
import pandas as pd
import time


global df
#create webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
DRIVER_PATH = '/path/to/chromedriver'
service = ChromeService(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

#navigate to page in question (could be an input later)
driver.get("http://www.idph.state.il.us/envhealth/wnvsurveillance_data_17.htm")

#get the html
html = driver.find_element(By.TAG_NAME, "center").get_attribute("outerHTML")

#get the table with pandas and put it in an excel sheet
df_list = pd.read_html(html)
df = df_list[2]

#get all the rows to be entered into the final dataframe later
counties = df["County"]


df.to_excel("county.xlsx", index=False)

#get all links
tables = driver.find_elements(By.TAG_NAME, "table")
table = tables[2]
links = table.find_elements(By.XPATH, ".//a")
ls = []
for link in links:
    ls.append(link.get_attribute("href"))

driver.quit()
#create dataframe
df = pd.DataFrame(
    {
        "Municipality": ["Test"],
        "Date Collected": ["11/25/2013"],
        "Animal/Insect": ["Mosquito"],
        "County": ["NaN"]

    }
)

#function that: gets the page source, grabs the data frame, then appends it to the dataframe
def getPageSource(i, lnk):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(lnk)

    html = driver.page_source

    temp_df_list = pd.read_html(html)
    temp_df = temp_df_list[2]

    num = len(temp_df.index) + 1
    series = pd.Series([counties[i] for _ in range(num)])
    temp_df = temp_df.assign(County = series)
    
    
    global df
    df = df.append(temp_df)
    driver.quit()


#append each table from each link to the data frame
for i, link in enumerate(ls):
    
    getPageSource(i, link)

#save it all to an excel file
df.to_excel("final_with_counties.xlsx", index=False)


    
