from rvaapp.models import *
import datetime

COMP_AER = {'AA': 'American Airlines', 'AS': 'Alaska Airlines', 'B6': 'JetBlue Airways', 'DL': 'Delta Airlines',
            'F9' : 'Frontier Airlines', 'HA': 'Hawaiian Airlines', 'NK' : 'Spirit Airlines', 'EV' : 'Atlantic Southeast Airlines',
            'OO' : 'SkyWest Airlines', 'UA': 'United Airlines', 'VX':'Virgin America', 'WN':'Southwest Airlines'}

def convert_time(time):
	hr = int(time/100)
	mn = time - (hr*100)
	mnt =hr*60 + mn
	return mnt

def load_data_init(data_file):
	sof = SetOfPlace("Aeroport")
	sof.data_from_csv(data_file)
	return sof


def creat_dataframe(csv_file):
	dataf = pd.read_csv(csv_file,sep="\t")
	dataf = dataf.drop('Unnamed: 0',axis=1)
	return dataf

def fill_df(df, csv_file_dh, ca_val, city_or, aero_or, date_or, time_or, city_ar, aero_ar, time_ar):
	decalage_horaire  = pd.read_csv(csv_file_dh,sep="\t")
	decalage_horaire = decalage_horaire.set_index('Unnamed: 0')

	list_mois = [31,28,31,30,31,30,31,31,30,31,30,31]
	if int(date_or.split('-')[0])%4 == 0:
		list_mois[1] = 29
	mois_cum = [sum(list_mois[0:x]) for x in range(len(list_mois)+1)] 
    
	ann = int(date_or.split('-')[0])
	mois = int(date_or.split('-')[1])
	jour = int(date_or.split('-')[2])
	dat = datetime.datetime(ann, mois, jour)    
    
	df.MONTH = mois
	df.DAY_OF_MONTH = jour
	df.DAY_OF_WEEK = dat.weekday() + 1
	df.CRS_DEP_TIME = int(time_or.split(':')[0])*100 + int(time_or.split(':')[1])
	df.CRS_ARR_TIME = int(time_ar.split(':')[0])*100 + int(time_ar.split(':')[1])
	df.CRS_ELAPSED_TIME = decalage_horaire.loc[city_ar,city_or] + (convert_time(df.CRS_ARR_TIME)- convert_time(df.CRS_DEP_TIME)) 
	df.DAY_OF_YEAR = mois_cum[mois-1] + jour
	df[aero_or] = 1
	df[aero_ar] = 1
	df['CARRIER_{}'.format(ca_val)] = 1 
	return df
