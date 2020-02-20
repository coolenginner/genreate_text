from lxml import html, etree
import requests
import re
import os
import csv
import sys
import argparse
import json
import datetime
import selenium
from datetime import datetime
from pathlib import Path
from bs4 import BeautifulSoup
import re

schedule_data = []
new_data = []
area_dict = {} 

def itterate():
    #read area data
    temp = []
    f = open("area.ini", "r")
    temp = f.readlines()
    for item in temp:
        str = item.strip('\n')
        key = str.split(',')[0]
        value = str.split(',')[1]
        area_dict[key] = value
    f.close()
     
    #read csv data
    with open("schedule.csv", 'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for row in csv_reader:
            if i != 0:
                new_temp = []
                new_temp.append(row[0])
                new_temp.append(row[1])
                new_temp.append(row[2])
                new_temp.append(row[3])
                new_temp.append(row[4])
                schedule_data.append(new_temp)
            i = i + 1

    stage = 'stage1'
    stage = stage.strip('stage')
    for row in schedule_data:
        if(int(stage) >= int(row[3])):
            new_data.append(row)

    #Make result data        
    res_temp = []
    for i in range(1,31):
        res_new_temp = []
        for row in new_data:
            if i == int(row[0]):
                res_new_temp.append(row)
        
        if res_new_temp:
            res_temp.append(res_new_temp)

    f = open("generatemonthlyschedule.txt","w")
    myfinal = ''    
    for row in res_temp:
        res_text = row[0][0] + '/02/2020'
        for key in area_dict:
            res_text = res_text + '\n' + area_dict[key] + ':'
            i = 0
            for col in row:
                if(key in col[4]):
                    if i == 0:res_text = res_text + col[1] + '-' + col[2]
                    else:res_text = res_text + '&&' + col[1] + '-' + col[2]
                    i = i + 1
            if i == 0:res_text = res_text + 'No Loadshedding'
        print(res_text)
        print('\n')
        myfinal = myfinal +  res_text + '\n\n'
        
    f.write(myfinal)
    f.close() 

    # print(new_data)

    # f.close()
	# try:
	# 	m = re.search(r'(.+)@(.+)\.(.+)', companyname)
	# 	if m:
	# 		appellation = m.groups()[1]
	# except:
	#    print("No email format")
	#    return
	# print("Fetching job details for {}.".format(appellation))
	# job_litsting_url = 'https://www.glassdoor.com/Job/jobs.htm'
	# parse(appellation, job_litsting_url)
	# scraped_data = getDescriptions(job_listings)

	# print("Writing data to output file '{}/{}s-job-results.csv'".format(name,appellation))
	# print("*********************Report**********************")
	# print("Company Name: {}".format(appellation))
	# print("Current Job Numbers: {}".format(len(scraped_data)))
	# print("Scrape Date: {}".format(datetime.now().strftime("%H:%M:%S,%m/%d/%Y")))

	# Path('{}'.format(name)).mkdir(parents=True, exist_ok=True)

	# with open('{}/{}s-job-results.csv'.format(name,appellation), 'wb') as csvfile:
	# 	fieldnames = ['Name', 'Company', 'State', 'City', 'Salary', 'Location', 'Description','Url']
	# 	writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_ALL)
	# 	writer.writeheader()
	# 	if scraped_data:
	# 		for data in scraped_data:
	# 			writer.writerow(data)
	# 	else:
	# 		print("Hey {}! Your search for {}s, it does not match any jobs".format(name,appellation))

itterate()
