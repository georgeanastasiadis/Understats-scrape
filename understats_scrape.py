from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd

#Create a session and load the page
website = "https://understat.com/league/Ligue_1/2021"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(website)

#Parse HTML and grab table data
soup = BeautifulSoup(driver.page_source, 'lxml')
tables = soup.find_all('table')

#Read tables
df = pd.read_html(str(tables))

print("The number of tables at site is:",len(df))

#We want the team overall table only
team_table = df[0]
team_table.to_csv("Ligue1-s2122.csv", index=False)

driver.quit()



