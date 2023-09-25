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

def get_batsman_name( url    ):
    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # match_data = wait.until(EC.presence_of_element_located((By.XPATH, " //table[@class='ds-w-full ds-table ds-table-md ds-table-auto  ci-scorecard-table']/tbody")))

    batter_names = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='ds-w-0 ds-whitespace-nowrap ds-min-w-max ds-flex ds-items-center']")))

    batter_names = [ batter.text for batter in batter_names ]

    return batter_names



def get_All(url):

    driver.get(url)
    wait = WebDriverWait(driver, 10)

    # match_data = wait.until(EC.presence_of_element_located((By.XPATH, " //table[@class='ds-w-full ds-table ds-table-md ds-table-auto  ci-scorecard-table']/tbody")))

    all = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//tbody//tr")))

    all_data = [ batter.text for batter in all ]

    return all_data


def get_batsman_and_bowler_data(raw_list):

    batsman_data = []
    bowler_data = []


    for sublist in raw_list:

        for item in sublist:


            if item.count('\n') == 2:
                batsman_data.append(item)

            if item.count('\n') == 1 and "not out" in item:
                batsman_data.append(item)

            if item.count('\n') == 3 :

                bowler_data.append(item)

            


    return batsman_data, bowler_data


def make_csv(file_name, headers, *lists):
    csv_filename = file_name + ".csv"

    # Transpose the lists to have them as columns in the CSV
    transposed_lists = list(zip(*lists))

    # Write the transposed lists with headers to the CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(headers)

        # Write each transposed list as a row in the CSV file
        for row in transposed_lists:
            writer.writerow(row)

    print(f"CSV file '{csv_filename}' has been created.")



def filter_list(data):

    keywords_to_filter = [
    "Extras", "TOTAL", "Did not bat", "Fall of wickets", "Toss", "Series", "Season", "Player",
    "Match number", "Hours of play", "Match days", "Umpires", "Reserve Umpire", "Match Referee",
    "TV Umpire",
    "Points", "PAK", "SL", "AUS", "NZ", "ZIM", "CAN", "KENYA", "SA", "IND", "ENG", "WI", "BAN",
    "IRE", "NED"
]

# Create a new 2D list with filtered data
    filtered_data = []

    for sublist in data:
        filtered_sublist = []

        for item in sublist:
            # Check if any keyword starts the line
            if any(item.strip().startswith(keyword) for keyword in keywords_to_filter) or len(item) == 0: 
                # If a keyword is found, skip this line
                continue
            else:
                filtered_sublist.append(item)

        filtered_data.append(filtered_sublist)

    # Print the filtered data
    return filtered_data




def process_batsman_data(batting_data, all_person_batting, total_runs, total_balls, total_fours, total_sixes, total_minutes_played, strike_rate):
    for data in batting_data:
        split_str = data.split("\n")
        
        if len(split_str) == 2:
            parts = split_str[1].split()
            if len(parts) >= 8:
                all_person_batting.append(split_str[0])
                total_runs.append(parts[2])
                total_balls.append(parts[3])
                total_minutes_played.append(parts[4])
                total_fours.append(parts[5])
                total_sixes.append(parts[6])
                strike_rate.append(parts[7])
        elif len(split_str) == 3:
            all_person_batting.append(split_str[0])
            total_runs.append(split_str[2].split(" ")[0])
            total_balls.append(split_str[2].split(" ")[1])
            total_minutes_played.append(split_str[2].split(" ")[2])
            total_fours.append(split_str[2].split(" ")[3])
            total_sixes.append(split_str[2].split(" ")[4])
            strike_rate.append(split_str[2].split(" ")[5])



       


            


        
        

if __name__ == "__main__":


    match_urls = [
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-india-1st-match-group-b-433558/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/kenya-vs-new-zealand-2nd-match-group-a-433559/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-canada-3rd-match-group-a-433560/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-zimbabwe-4th-match-group-a-433561/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-netherlands-5th-match-group-b-433562/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/kenya-vs-pakistan-6th-match-group-a-433563/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/south-africa-vs-west-indies-7th-match-group-b-433564/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-new-zealand-8th-match-group-a-433565/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-ireland-9th-match-group-b-433566/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-pakistan-10th-match-group-a-433567/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-england-11th-match-group-b-433568/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-zimbabwe-12th-match-group-a-433570/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/netherlands-vs-west-indies-13th-match-group-b-433569/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-kenya-14th-match-group-a-433571/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-ireland-15th-match-group-b-433572/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/netherlands-vs-south-africa-16th-match-group-b-433573/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-pakistan-17th-match-group-a-433574/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-zimbabwe-18th-match-group-a-433575/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-west-indies-19th-match-group-b-433576/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-australia-20th-match-group-a-433577/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-south-africa-21st-match-group-b-433579/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-ireland-22nd-match-group-b-433578/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-kenya-23rd-match-group-a-433580/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-pakistan-24th-match-group-a-433581/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-netherlands-25th-match-group-b-433582/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-zimbabwe-26th-match-group-a-433583/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/ireland-vs-west-indies-27th-match-group-b-433584/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-england-28th-match-group-b-433585/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-south-africa-29th-match-group-b-433586/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/canada-vs-new-zealand-30th-match-group-a-433587/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-kenya-31st-match-group-a-433588/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-netherlands-32nd-match-group-b-433590/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/pakistan-vs-zimbabwe-33rd-match-group-a-433589/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/ireland-vs-south-africa-34th-match-group-b-433591/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-canada-35th-match-group-a-433592/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/england-vs-west-indies-36th-match-group-b-433593/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/ireland-vs-netherlands-37th-match-group-b-433595/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-sri-lanka-38th-match-group-a-433594/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/bangladesh-vs-south-africa-39th-match-group-b-433597/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/australia-vs-pakistan-40th-match-group-a-433596/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/kenya-vs-zimbabwe-41st-match-group-a-433598/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-west-indies-42nd-match-group-b-433599/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/pakistan-vs-west-indies-1st-quarter-final-433600/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-australia-2nd-quarter-final-433601/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/new-zealand-vs-south-africa-3rd-quarter-final-433602/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-england-4th-quarter-final-433603/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/sri-lanka-vs-new-zealand-1st-semi-final-433604/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-pakistan-2nd-semi-final-433605/full-scorecard",
        "https://www.espncricinfo.com/series/icc-cricket-world-cup-2010-11-381449/india-vs-sri-lanka-final-433606/full-scorecard"



    ]

    total_data = []

    for url in match_urls:

        rows = get_All(url)
        total_data.append(rows)
        
    temp = filter_list(total_data)

    # print(temp)

    


    
    batsman_data, bowler_data = get_batsman_and_bowler_data(temp)

    print(batsman_data)

    print("--------------------------------------------------")
    print("--------------------------------------------------")


    print(bowler_data)



    all_persons_batting =[]
    total_runs, total_balls, total_fours, total_sixes , total_minutes_played , strike_rate = [], [], [], [],[],[]
    headers = ["Name", "Runs", "Balls", "Minutes Played", "Fours", "Sixes", "Strike Rate"]


    process_batsman_data(batsman_data ,all_persons_batting , total_runs , total_balls , total_fours , total_sixes , total_minutes_played , strike_rate)

    make_csv("batsman_data" , headers , all_persons_batting , total_runs , total_balls , total_fours , total_sixes , total_minutes_played , strike_rate)

   
while True:
    pass  





# [
#     "Virender Sehwag \nb Shakib Al Hasan\n175 140 198 14 5 125.00",
#     "Sachin Tendulkar \nrun out (Shakib Al Hasan/†Mushfiqur Rahim)\n28 29 46 4 0 96.55",
#     "Gautam Gambhir \nb Mahmudullah\n39 39 49 3 0 100.00",
#     "Virat Kohli \nnot out 100 83 113 8 2 120.48",
#     "Yusuf Pathan \nc †Mushfiqur Rahim b Shafiul Islam\n8 10 10 0 0 80.00",
#     "Tamim Iqbal \nc Yuvraj Singh b Patel\n70 86 136 3 1 81.39",
#     "Imrul Kayes \nb Patel\n34 29 33 7 0 117.24",
#     "Zunaed Siddique \nst †Dhoni b Harbhajan Singh\n37 52 66 1 1 71.15",
#     "Shakib Al Hasan (c)\nc Harbhajan Singh b Pathan\n55 50 65 5 0 110.00",
#     "Mushfiqur Rahim †\nc sub (SK Raina) b Khan\n25 30 39 2 0 83.33",
#     "Raqibul Hasan \nnot out 28 28 44 0 1 100.00",
#     "Mahmudullah \nb Patel\n6 6 6 0 0 100.00",
#     "Naeem Islam \nlbw b Patel\n2 8 8 0 0 25.00",
#     "Abdur Razzak \nlbw b Khan\n1 5 6 0 0 20.00",
#     "Shafiul Islam \nrun out (Harbhajan Singh)\n0 1 1 0 0 0.00",
#     "Rubel Hossain \nnot out 1 6 4 0 0 16.66",
#     "Raqibul Hasan\nnot out 28 28",
#     "Rubel Hossain\nnot out 1 6",
# ]


# [
#     "Shafiul Islam\n7 0 69\n1\n9.85 15 8 1 2 1",
#     "Shakib Al Hasan\n10 0 61\n1\n6.10 23 4 1 3 0",
#     "Mahmudullah\n7 0 49\n1\n7.00 15 3 1 3 0",
#     "Zaheer Khan\n10 0 40\n2\n4.00 35 2 0 4 0",
#     "Munaf Patel\n10 0 48\n4\n4.80 37 3 2 0 0",
#     "Harbhajan Singh\n10 0 41\n1\n4.10 26 1 0 1 0",
#     "Yusuf Pathan\n8 0 49\n1\n6.12 12 3 0 2 0",
# ]



