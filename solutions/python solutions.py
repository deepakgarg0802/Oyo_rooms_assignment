import pandas
import numpy
from collections import defaultdict
import datetime

class Oyo :
	
	def __init__(self,values=None):
		""" Answer 1 :
		The constructor will import datasets provided
		here we are given tables for jan,feb,mar and a city table"""

		self.tableAcsv= pandas.DataFrame.from_csv("./TableA.csv", index_col=None)
		self.tableBcsv= pandas.DataFrame.from_csv("./TableB.csv", index_col=None)
		self.tableCcsv= pandas.DataFrame.from_csv("./TableC.csv", index_col=None)
		self.cityTable= pandas.read_excel("TableD.xlsx")
		print "Importing all files done, Solution 1 completed.."

	def answer_2_and_3(self,values=None):
		""" Answer 2 and 3:
		This function will Extract unique users for each month and 
		calculate total number of bookings made by each, total amount spent in each month,
		total room nights stayed (status2) for each user for each month."""		

		#declare variables for column numbers
		no_of_bookings_jan=0
		total_room_nights_jan=1
		total_amount_jan=2

		no_of_bookings_feb=3
		total_room_nights_feb=4
		total_amount_feb=5

		no_of_bookings_mar=6
		total_room_nights_mar=7
		total_amount_mar=8

		empty=[0,0,0,0,0,0,0,0,0] #to initialize empty row

		all_users={}
		all_users=defaultdict(lambda:empty)


		#-------add users from January table--------
		for index,row in self.tableAcsv.iterrows() :

		    all_users[row['customer_id']][no_of_bookings_jan] += 1
		    all_users[row['customer_id']][total_amount_jan] += row['amount']
		    if (row['status']==2) :
		        
		        x=(datetime.datetime.strptime(row['checkout'],"%m/%d/%Y")-datetime.datetime.strptime(row['checkin'],"%m/%d/%Y")).days
		        x= x* row['oyo_rooms']
		        all_users[row['customer_id']][total_room_nights_jan] += x
		    empty=[0,0,0,0,0,0,0,0,0]


		#-------add users from February table--------
		for index,row in self.tableBcsv.iterrows() :
    
		    all_users[row['customer_id']][no_of_bookings_feb] += 1
		    all_users[row['customer_id']][total_amount_feb] += row['amount']
		    if (row['status']==2) :
		        
		        x=(datetime.datetime.strptime(row['checkout'],"%m/%d/%Y")-datetime.datetime.strptime(row['checkin'],"%m/%d/%Y")).days
		        x= x* row['oyo_rooms']
		        all_users[row['customer_id']][total_room_nights_feb] += x
		    empty=[0,0,0,0,0,0,0,0,0]

		#-------add users from March table--------
		for index,row in self.tableCcsv.iterrows() :
    
		    all_users[row['customer_id']][no_of_bookings_mar] += 1
		    all_users[row['customer_id']][total_amount_mar] += row['amount']
		    if (row['status']==2) :
		        
		        x=(datetime.datetime.strptime(row['checkout'],"%m/%d/%Y")-datetime.datetime.strptime(row['checkin'],"%m/%d/%Y")).days
		        x= x* row['oyo_rooms']
		        all_users[row['customer_id']][total_room_nights_mar] += x
		    empty=[0,0,0,0,0,0,0,0,0]

		#--------------convert result to a dataframe------
		df1= pandas.DataFrame(all_users)
		df1= df1.transpose()
		df1.columns=["no_of_bookings_jan","total_room_nights_jan","total_amount_jan",
		             "no_of_bookings_feb","total_room_nights_feb","total_amount_feb",
		             "no_of_bookings_mar","total_room_nights_mar","total_amount_mar"]
		df1.index.name= "Guest_id"

		#--------write results to csv file------
		df1.to_csv("./unique_user_data.csv")
		print "answer 2 's csv file generated as unique_user_data.csv"

	def answer_4(self,values=None):
		"""answer 4 :
		the function calculates Repeat Rate for the month February"""

		jan_customers= set(self.tableAcsv.customer_id) #unique customers in january
		feb_customers= set(self.tableBcsv.customer_id) #unique customers in february
		both_customers= jan_customers-(jan_customers-feb_customers) ##unique customers present in both months

		repeat_rate_feb= len(both_customers)*100.0/len(jan_customers) #repeat rate will be (intersection/customers_in_jan  *100)

		print "Repeat rate required is :",repeat_rate_feb

	def answer_5(self,values=None):
		"""answer 5 : 
		this function gives the top 3 revenue earning hotels 
		over this time period for each city"""

		#------ selecting required columns from dataset----------
		tableAcsv= self.tableAcsv[["hotel_id","amount"]]
		tableBcsv= self.tableBcsv[["hotel_id","amount"]]
		tableCcsv= self.tableCcsv[["hotel_id","amount"]]

		#-------concatenate data for all hotels-------
		frames= [tableAcsv,tableBcsv,tableCcsv]
		data= pandas.concat(frames)

		#--------aggregate Revenue= total amount paid by grouping by hotel_id-------		
		data=data.groupby('hotel_id',as_index=False)
		revenue_table=data.sum()

		#-------- Inner join to associate city with hotel_id-------
		merged= pandas.merge(revenue_table,self.cityTable,on='hotel_id',how='inner')

		#sort based on Revenue
		merged.sort_values('amount', ascending=False, inplace=True)
		x = merged.groupby('city').apply(self.ranker) # Dense ranking of hotels


		ans=x[(x.hotel_rank>=1) & (x.hotel_rank <= 3)].sort_values(['city','hotel_rank']) #Selecting top 3 hotels only
		
		#------refine results-----------
		ans=ans.reset_index()
		ans= ans[["city","hotel_id","amount"]]

		#-----------write result to csv---------
		ans.to_csv("top_3_hotels.csv")
		print "answer 5 's csv file generated as top_3_hotels.csv"
		
	def ranker(self,df):
	    """Utility function :
	    	Assigns a rank to each hotel based on revenue, with 1 being the highest.
	    	Assumes the data is DESC sorted."""

	    df['hotel_rank'] = numpy.arange(len(df)) + 1
	    return df

if __name__== "__main__" :

	deepak_solution= Oyo()

	deepak_solution.answer_2_and_3()
	deepak_solution.answer_4()
	deepak_solution.answer_5()
	print "done"