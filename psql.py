import psycopg2
try:
	conn = psycopg2.connect("host=192.168.1.14 dbname=ttd user=postgres")


	cur = conn.cursor()
	#postgreSQL_select_Query = "SELECT timestamp ipaddress, rurl, tdid, puid from match_table limit 6"
	postgreSQL_select_Query = "SELECT date(logentrytime), conversionid, advertiserid, conversiontype, tdid, ipaddress, referrerurl, monetaryvalue, monetaryvaluecurrency, orderid, processedtime from conversions limit 6" 
	cur.execute(postgreSQL_select_Query)
	#cur.execute('SELECT * FROM match_table')
	one = cur.fetchone()
	all = cur.fetchall()
	print("Query Successful!")

	for row in all:
		print("   ", row[0], "   ", row[1], "   ", row[2], "   ", row[3], "   ", row[4], "   ", row[5], "   ", row[6], "   ", row[7], "   ", row[8], "   ", row[9], "   ", row[10])
		#print("\nAll: \n")
except:
	print("I Am Not Able To Connect To The DB")
	print("I can't run select query 1!")
