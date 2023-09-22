import selenium
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re

chromedriver_path = "/Users/jaspreetSinghSodhi/downloads/chromedriver"

chrome_options = Options()
chrome_options.add_argument("--start-maximized") 

driver = webdriver.Chrome( options=chrome_options)


def get_data(): 
                
    driver.get('https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/match-schedule-fixtures-and-results')

    wait  =   WebDriverWait(driver, 5)

    match_dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='ds-p-0']//div[@class='ds-text-compact-xs ds-font-bold ds-w-24']")))

    teams = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//p[@class='ds-text-tight-m ds-font-bold ds-capitalize ds-truncate']")))

    winning_margins = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//p[@class='ds-text-tight-s ds-font-regular ds-line-clamp-2 ds-text-typo']")))
    all_matches_date = []
    team1 = []
    team2 = []



    for match in match_dates:
        all_matches_date.append(match.text)

    

    for i  , team in enumerate(teams):

        if i % 2 == 0:
            team1.append(team.text)
        
        else:
            team2.append(team.text)


    for i in range(len(team1)):
        print(team1[i])
        print(team2[i])
        
        
    for margin in winning_margins:
        print(margin.text)
        print("---------------------------------------------------")




  



if __name__ == "__main__":
    get_data()
    while True:
        pass  


# OUTPUT format 

# Sat, 19 Feb '11
# RESULT • 
# 1st Match, Group B (D/N) • Mirpur, ICC Cricket World Cup
# India
# 370/4
# Bangladesh
# (50 ov, T:371) 283/9
# India won by 87 runs
# Report
# Photos
# Videos