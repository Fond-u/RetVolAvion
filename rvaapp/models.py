# coding: utf-8
import pandas as pd
import numpy as np

class SetOfPlace:
	def __init__(self, name):
		self.name = name

	def data_from_csv(self, csv_file):
		self.dataframe = pd.read_csv(csv_file, sep="\t", low_memory=False)
	
	def get_state(self, comp_aer):
		datastate = self.dataframe[self.dataframe.CARRIER == comp_aer]
		origin_state = datastate.ORIGIN_STATE_NM.unique()
		return np.sort(origin_state)

	def get_city(self, comp_aer, state):
		datastate = self.dataframe[self.dataframe.CARRIER == comp_aer]
		datacity = datastate[datastate.ORIGIN_STATE_NM == state]
		origin_city = datacity.ORIGIN_CITY_NAME.unique()
		return np.sort(origin_city)

	def get_aero(self, comp_aer, state, city):
		datastate = self.dataframe[self.dataframe.CARRIER == comp_aer]
		datacity = datastate[datastate.ORIGIN_STATE_NM == state]
		aeroport = datacity[datacity.ORIGIN_CITY_NAME == city]
		aeroport_org = aeroport.ORIGIN.unique()
		return np.sort(aeroport_org)

	def get_state_dest(self, comp_aer):
		datastate = self.dataframe[self.dataframe.CARRIER == comp_aer]
		dest_state = datastate.DEST_STATE_NM.unique()
		return np.sort(dest_state)

	def get_city_dest(self, comp_aer, state):
		datastate = self.dataframe[self.dataframe.CARRIER == comp_aer]
		datacity = datastate[datastate.DEST_STATE_NM == state]
		dest_city = datacity.DEST_CITY_NAME.unique()
		return np.sort(dest_city)

	def get_aero_dest(self, comp_aer, state, city):
		datastate = self.dataframe[self.dataframe.CARRIER == comp_aer]
		datacity = datastate[datastate.DEST_STATE_NM == state]
		aeroport = datacity[datacity.DEST_CITY_NAME == city]
		aeroport_dest = aeroport.DEST.unique()
		return np.sort(aeroport_dest)

