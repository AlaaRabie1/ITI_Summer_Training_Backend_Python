import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

job_title = []
company_name = []
location_name = []
skills = []
links = []
salaries = []
job_requirements = []
dates = []

page_number = 0
while True:
    try:
        result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={page_number}")

        src = result.content

        soup = BeautifulSoup(src, "lxml")

        page_limit = int(soup.find("strong").text)
        
        if(page_number > page_limit // 15 ):
            print("Pages ended, terminate")
            break

        # extarcting job titles, job skills, company names, location names
        jobs = soup.find_all("div" , {'class': 'css-1gatmva e1v1l3u10'})
        number_of_jobs = len(jobs)

        job_names = soup.find_all("h2" , {'class': 'css-m604qf'})

        company_names = soup.find_all("a" , {'class': 'css-17s97q8'})

        location_names = soup.find_all("span" , {'class': 'css-5wys0k'})

        job_cards = soup.find_all("div", {'class': 'css-y4udm8'})

        job_skills = []

        posted_new = soup.find_all("div", {'class': 'css-4c4ojb'})

        postesd_old = soup.find_all("div", {'class': 'css-do6t5g'})

        posted = [*posted_new, *postesd_old]

        for job in job_cards:
            inner_divs = job.find_all("div")
            
            if len(inner_divs) >= 2:
                job_skill = inner_divs[1]  # .get_text(separator="").strip()
                job_skills.append(job_skill)
                

        # loop over the current lists to extract the needed info into other lists
        for i in range(number_of_jobs):
            job_title.append(job_names[i].text)
            links.append(job_names[i].find("a").attrs['href'])
            company_name.append(company_names[i].text.replace("-","").strip())
            location_name.append(location_names[i].text)
            skills.append(job_skills[i].text)
            date_text = posted[i].text.replace("-", "").strip()
            dates.append(date_text)

        page_number = page_number + 1
        print("Page switched")
        
    except:
        print("error occured")
        break

# now if we want to get info from inner pages -> salary, job requirements
# for link in links:
#     page = requests.get(link)
#     src = page.content
#     soup = BeautifulSoup(src, "lxml")
#     salary = soup.find("span", {'class': 'css-4xky9y'})
#     salaries.append(salary.text.strip())
#     requirements_list = soup.find("div", {'class': 'css-1t5f0fr'}).ul
#     requirement = ""
#     for li in requirements_list.find_all("li"):
#         requirement += li.text+" | "
#     requirement = requirement[:-2]
#     job_requirements.append(requirement)


# csv file to fill it with the data we extracted
file_list = [job_title, company_name, dates, location_name, skills, links, salaries, job_requirements]

# ziplongest pairs the elements from each list into another list
exported = zip_longest(*file_list) # unpacking the list into exported
with open("G:\ITI_Summer_training_Backend\Day4\jobstest.csv", 'w', newline='', encoding='utf-8') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title", "Company Name", "Date", "Location", "Skill", "Link", "Salary", "Requirements"])
    wr.writerows(exported)
    print("file created")

