import csv
from random import uniform, randint
import datetime
from os import getcwd


# diagonal :  46.7384E , 39.7500N  -->  46.7408, 39.7515
header = ['longitude' ,   'latitude','datetime','height' ,'wind_velocity_x','wind_velocity_y','pressure' , 'temperature', 'bird_amount']
def random_data(writer, lat , long , date ):
    data=[]
    passed=datetime.timedelta(seconds=0)
    max=datetime.timedelta(days=1)
    amount=randint(0,30)
    if(amount!=0):
        data.append(lat)
        data.append(long)
        data.append(   datetime.datetime.strptime('01:01:2022:00:00:00', "%d:%m:%Y:%H:%M:%S") +datetime.timedelta(days=date) )
        passed=datetime.timedelta(seconds=0)
        max=datetime.timedelta(days=1)
        while(passed<max):
            time_delta=datetime.timedelta(hours=randint(0,24) , minutes=randint(0,60) , seconds=randint(0,60))
            passed+=time_delta
            if(passed+time_delta<max):
                data[2]+=time_delta
                rest=data[:3]
                rest.append( round(uniform(0, 50) , 2))
                rest.append(round(uniform(0,20) , 1  ))
                rest.append(round(uniform(0,20) , 1  ))
                rest.append(round(uniform(0.99 , 1.02) , 2  ))
                rest.append(round(uniform(0,30) , 1  ))
                rest.append(amount)
                writer.writerow(rest)
def create(s,n, w,e ,sensors_on_latitude,  sensors_on_longitute):
    with open(getcwd()+'/data files/randomdata.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        for k in range(365):
            for j in range(sensors_on_latitude):
                for i in range(sensors_on_longitute):
                    random_data( writer ,round( s+ (n-s)/sensors_on_latitude*j , 4), round( w+(e-w)/sensors_on_longitute*i,4), k )