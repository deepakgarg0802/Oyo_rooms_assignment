import csv
import pandas
from collections import defaultdict
# with open('TableA.csv','rb') as f:
# 	reader= csv.reader(f)
# 	for row in reader:
# 		print row

tableAcsv= pandas.DataFrame.from_csv("TableB.csv", index_col=None)
empty=[0,0,0,0]
all_users={}

all_users=defaultdict(int)

for index,row in tableAcsv.iterrows() :
	#	print all_users[row['customer_id']]
	all_users[row['customer_id']] += 1
print (all_users)
