import requests
from bs4 import BeautifulSoup
import csv


date = input("Please enter a Date in the following format MM/DD/YYYY: ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")

def main(page):

    src = page.content # code of the page (byte code)

    # parsing converts the byte code into a readable code
    soup = BeautifulSoup(src, "lxml")
    matches_details = []

    championships = soup.find_all("div" , {'class': 'matchCard'})  # to filter the code i want by specfic class

    def get_match_info(championships):
        championship_title = championships.contents[1].find("h2").text.strip()
        all_matches = championships.contents[3].find_all("div" , {'class': 'future'})
        number_of_matches = len(all_matches)
        
        for i in range(number_of_matches):
            # get teams names
            team_A = all_matches[i].find("div", {'class': 'teamA'}).text.strip()
            team_B = all_matches[i].find("div", {'class': 'teamB'}).text.strip()

            # get score
            match_result = all_matches[i].find("div", {'class': 'MResult'}).find_all("span", {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"

            # get match time 
            match_time = all_matches[i].find("div", {'class': 'MResult'}).find("span", {'class': 'time'}).text.strip()

            # add match info to matches_details
            matches_details.append({'نوع البطولة': championship_title, 'الفريق الاول': team_A, 'الفريق التاني': team_B,
                                     'ميعاد المباراة': match_time, 'النتيجة': score})


    for i in range(len(championships)):
        get_match_info(championships[i])

    keys = matches_details[0].keys()

    with open('G:\ITI_Summer_training_Backend\Day4\match-details.csv', 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("file created")


main(page)