from analyseandpredict import predictor, plan_analyser
from randomdata import create
[s,n]=map(float, input("Longitute from, to(In East direction): ").strip().split() )
[w,e]=map(float, input("Latitude from, to(In North direction): ").strip().split() )

#s , n=44 , 50
#w, e=34, 40

# 40.7128° N, 74.0060W  (New York)
#n=40.6
#s=40.8256
#w=-74.812
#e=-74.2
create(s, n, w, e,10, 10)
plan_analyser(s,n, w,e,'data files/randomdata.csv')
predictor(s, n, w, e,5, 'data files/randomdata.csv' )
