from os import getcwd
from area_to_image import area_to_image
from adder import adder
import csv

def affects(coords  , line ,R=10):
    return (coords[0]- float(line['longitude']))**2 +(coords[1]-float(line['latitude']))**2<=R**2

def plan_analyser(s, n, w,e , filename =getcwd() +"/data files/data.csv", acc=4 ):
    area_to_image(n, s, w, e )
    list =[ [round(c[0], acc ), round(c[1] , acc)] for c in adder(s,n,w,e)]
    #print(list)
    bird_list=[]
    data=open(filename)
    for line in csv.DictReader(data):
        for coords in list:
            if affects(coords, line):
                bird_list.append(int(line['bird_amount']) )
    print(sum(bird_list) , 'birds would be attracted.' )

#plan_analyser(s,n , w,e)


def predictor(s, n ,w,e, Planned_Amount ,filename ="data.csv"):
    location_dictionary={}
    data=open(filename)
    for line in csv.DictReader(data):
        if(s<=float(line['longitude']) <=n  and w<=float(line['latitude']) <=e):
            key=line['longitude']+','+line['latitude']
            birds=int(line['bird_amount'])
            if(key in location_dictionary):
                location_dictionary[key].append(birds)
            else:
                location_dictionary[key]=[birds]
    #print( location_dictionary.items())
    k= dict(    sorted(     location_dictionary.items() , key= lambda x: sum( location_dictionary[x[0]] )        ))
    all_birds=0  
    n=0                   
    for i in k:
        n+=1
        if(n<=Planned_Amount):
            print("Coordinates:" , i,"Passed birds:", sum(k[i]) )
            all_birds+=sum(k[i])
        else:
            break
    print("ALL BIRDS: " , all_birds)