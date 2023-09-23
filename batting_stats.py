import csv
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

def match_details( url , batting_list_team1  ):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    match_data = wait.until(EC.presence_of_element_located((By.XPATH, " //table[@class='ds-w-full ds-table ds-table-md ds-table-auto  ci-scorecard-table']/tbody")))

    batting_list_team1.append(match_data.text)



        

if __name__ == "__main__":


    match_urls = [
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-india-1st-match-group-b-433558/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/kenya-vs-new-zealand-2nd-match-group-a-433559/full-scorecard"
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-canada-3rd-match-group-a-433560/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-zimbabwe-4th-match-group-a-433561/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-netherlands-5th-match-group-b-433562/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/kenya-vs-pakistan-6th-match-group-a-433563/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/south-africa-vs-west-indies-7th-match-group-b-433564/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-new-zealand-8th-match-group-a-433565/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-ireland-9th-match-group-b-433566/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-pakistan-10th-match-group-a-433567/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-england-11th-match-group-b-433568/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-zimbabwe-12th-match-group-a-433570/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/netherlands-vs-west-indies-13th-match-group-b-433569/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-kenya-14th-match-group-a-433571/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-ireland-15th-match-group-b-433572/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/netherlands-vs-south-africa-16th-match-group-b-433573/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-pakistan-17th-match-group-a-433574/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-zimbabwe-18th-match-group-a-433575/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-west-indies-19th-match-group-b-433576/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-australia-20th-match-group-a-433577/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-south-africa-21st-match-group-b-433579/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-ireland-22nd-match-group-b-433578/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-kenya-23rd-match-group-a-433580/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-pakistan-24th-match-group-a-433581/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-netherlands-25th-match-group-b-433582/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-zimbabwe-26th-match-group-a-433583/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/ireland-vs-west-indies-27th-match-group-b-433584/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-england-28th-match-group-b-433585/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-south-africa-29th-match-group-b-433586/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-new-zealand-30th-match-group-a-433587/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-kenya-31st-match-group-a-433588/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-netherlands-32nd-match-group-b-433590/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/pakistan-vs-zimbabwe-33rd-match-group-a-433589/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/ireland-vs-south-africa-34th-match-group-b-433591/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-canada-35th-match-group-a-433592/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-west-indies-36th-match-group-b-433593/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/ireland-vs-netherlands-37th-match-group-b-433595/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-sri-lanka-38th-match-group-a-433594/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-south-africa-39th-match-group-b-433597/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-pakistan-40th-match-group-a-433596/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/kenya-vs-zimbabwe-41st-match-group-a-433598/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-west-indies-42nd-match-group-b-433599/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/pakistan-vs-west-indies-1st-quarter-final-433600/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-australia-2nd-quarter-final-433601/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-south-africa-3rd-quarter-final-433602/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-england-4th-quarter-final-433603/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-new-zealand-1st-semi-final-433604/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-pakistan-2nd-semi-final-433605/full-scorecard",
        # "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-sri-lanka-final-433606/full-scorecard"



    ]

    raw_team1_data = []
    final_batting_team1_data = []

    for url in match_urls:
        match_details(url , batting_list_team1=raw_team1_data)


        split_data = []

        for item in raw_team1_data:
             split_data.extend(item.split('\n'))

        
        filter_data = []

        for item in split_data:
            if item.startswith("Extras"):
                break
            filter_data.append(item)

        print(filter_data)
        final_batting_team1_data.append(filter_data)
        raw_team1_data.clear()
    
    print(final_batting_team1_data)






while True:
    pass  



# [
#     [
#         "Virender Sehwag ",  -- batsman name 
#         "b Shakib Al Hasan", 
#         "175 140 198 14 5 125.00",  - Runs , Balls , Minutes , 4s , 6s , Strike Rate
#         "Sachin Tendulkar ",
#         "run out (Shakib Al Hasan/†Mushfiqur Rahim)",
#         "28 29 46 4 0 96.55",
#         "Gautam Gambhir ",
#         "b Mahmudullah",
#         "39 39 49 3 0 100.00",
#         "Virat Kohli ",
#         "not out 100 83 113 8 2 120.48",
#         "Yusuf Pathan ",
#         "c †Mushfiqur Rahim b Shafiul Islam",
#         "8 10 10 0 0 80.00",
#     ],
#     [
#         "Alex Obanda ",
#         "lbw b Southee",
#         "6 19 27 0 0 31.57",
#         "Seren Waters ",
#         "lbw b Bennett",
#         "16 42 49 1 0 38.09",
#         "Collins Obuya ",
#         "lbw b Bennett",
#         "14 19 32 2 0 73.68",
#         "Steve Tikolo ",
#         "b Bennett",
#         "2 2 4 0 0 100.00",
#         "Morris Ouma †",
#         "lbw b Bennett",
#         "1 6 12 0 0 16.66",
#         "Rakep Patel ",
#         "not out 16 23 46 1 0 69.56",
#         "Jimmy Kamande (c)",
#         "c †BB McCullum b Oram",
#         "2 16 19 0 0 12.50",
#         "Thomas Odoyo ",
#         "c Ryder b Oram",
#         "2 6 6 0 0 33.33",
#         "Nehemiah Odhiambo ",
#         "b Southee",
#         "0 6 6 0 0 0.00",
#         "Shem Ngoche ",
#         "lbw b Southee",
#         "0 1 1 0 0 0.00",
#         "Elijah Otieno ",
#         "c Styris b Oram",
#         "0 4 4 0 0 0.00",
#     ],
# # ]
# [
#         "Virender Sehwag ",
#         "175 140 198 14 5 125.00",
#         "Sachin Tendulkar ",
#         "28 29 46 4 0 96.55",
#         "Gautam Gambhir ",
#         "39 39 49 3 0 100.00",
#         "Virat Kohli ",
#         "not out 100 83 113 8 2 120.48",
#         "Yusuf Pathan ",
#         "8 10 10 0 0 80.00",
#     ]