import csv
import pandas
from collections import defaultdict
import datetime


tableAcsv= pandas.DataFrame.from_csv("TableA.csv", index_col=None)
empty=[0,0,0,0]
all_users_of_jan={}

all_users_of_jan=defaultdict(lambda:empty)

for index,row in tableAcsv.iterrows() :
    #print row['customer_id']
    #print all_users[row['customer_id']]
    all_users_of_jan[row['customer_id']][0] += 1
    all_users_of_jan[row['customer_id']][1] += row['amount']
    if (row['status']==2) :
        
        x=(datetime.datetime.strptime(row['checkout'],"%m/%d/%Y")-datetime.datetime.strptime(row['checkin'],"%m/%d/%Y")).days
        x= x* row['oyo_rooms']
        all_users_of_jan[row['customer_id']][2] += x
    empty=[0,0,0,0]


tableBcsv= pandas.DataFrame.from_csv("TableB.csv", index_col=None)
empty=[0,0,0,0]
all_users_of_feb={}

all_users_of_feb=defaultdict(lambda:empty)

for index,row in tableBcsv.iterrows() :
    #print row['customer_id']
    #print all_users[row['customer_id']]
    all_users_of_feb[row['customer_id']][0] += 1
    all_users_of_feb[row['customer_id']][1] += row['amount']
    if (row['status']==2) :
        
        x=(datetime.datetime.strptime(row['checkout'],"%m/%d/%Y")-datetime.datetime.strptime(row['checkin'],"%m/%d/%Y")).days
        x= x* row['oyo_rooms']
        all_users_of_feb[row['customer_id']][2] += x
    empty=[0,0,0,0]

tableCcsv= pandas.DataFrame.from_csv("TableC.csv", index_col=None)
empty=[0,0,0,0]
all_users_of_mar={}

all_users_of_mar=defaultdict(lambda:empty)

for index,row in tableCcsv.iterrows() :
    #print row['customer_id']
    #print all_users[row['customer_id']]
    all_users_of_mar[row['customer_id']][0] += 1
    all_users_of_mar[row['customer_id']][1] += row['amount']
    if (row['status']==2) :
        
        x=(datetime.datetime.strptime(row['checkout'],"%m/%d/%Y")-datetime.datetime.strptime(row['checkin'],"%m/%d/%Y")).days
        x= x* row['oyo_rooms']
        all_users_of_mar[row['customer_id']][2] += x
    empty=[0,0,0,0]

df1= pandas.DataFrame(all_users_of_mar)
df1= df1.transpose()
df1.columns=["count","room_nights_stayed","amount","abc"]
print df1