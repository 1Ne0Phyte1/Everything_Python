import time
from bs4 import BeautifulSoup
import requests

print('Put some skill that you are not familiar with')
unfailiar_skill = input('>')
print(f"Filtering out {unfailiar_skill}")


def find_job():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    # print(job)
    for job in jobs:
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            # print(company_name)
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            # print(skills)
            more_info = job.header.h2.a['href']
            if unfailiar_skill not in skills:
                print(f"Company Name: {company_name.strip()}")
                print(f'Required Skills: {skills.strip()}')
                print(f"Published Date: {published_date.strip()}\n")
                print(f"More Info: {more_info}")


if __name__ == '__main__':
    while True:
        find_job()
        time_wait = 10
        print(f"waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
