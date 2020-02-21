import os
import csv
import sys

schedule_data = []
new_data = []
area_dict = {} 

def itterate():
    stage = '5'
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
                    else:
                        # print(res_text.split('-')[-1][:-3])
                        if int(res_text.split('-')[-1][:-3])>=int(col[1].rsplit(':', 1)[0]):
                            res_text = res_text.rsplit('-', 1)[0] + '-' + col[2]
                        else: res_text = res_text + '&&' + col[1] + '-' + col[2]
                    i = i + 1
            if i == 0:res_text = res_text + 'No Loadshedding'
        print(res_text)
        print('\n')
        myfinal = myfinal +  res_text + '\n\n'
        
    f.write(myfinal)
    f.close()
itterate()
