import numpy as np
import random
from flask import Flask, render_template, jsonify, request

from .utils import *

app = Flask(__name__)

app.config.from_object('config')

sof = load_data_init(app.config['DATAFLIGHT'])

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html') 


@app.route('/info/', methods=['GET', 'POST'])
def info():
	ca_val = False
	st_or = False
	st_ar = False
	city_or = False
	city_ar = False
	aero_or = False
	aero_ar = False
	date_or = False
	date_ar = False
	time_or = False
	time_ar = False
	step = 0 
	dt_not_valide = False 

	if request.method == 'POST':
		ca_val = request.form['ca']
		step = int(request.form['step'])

	if step > 1:
		st_or = request.form['st_or']

	if step > 2:
		city_or = request.form['ct_or']
	
	if step > 3:
		aero_or = request.form['ae_or']

	if step > 4:
		date_or = request.form['date_or']
		time_or = request.form['time_or']
		if date_or == '' or time_or == '':
			dt_not_valide = True
			step = 4
		else:
			dt_not_valide = False

	if step > 5:
		st_ar = request.form['st_ar']

	if step > 6:
		city_ar = request.form['ct_ar']

	if step > 7:
		aero_ar = request.form['ae_ar']

	if step > 8:
		date_ar = request.form['date_ar']
		time_ar = request.form['time_ar']

	return render_template('infoV.html', step_val = step, 
		ca_dict = COMP_AER, ca_val = ca_val, 
		st_or_list = sof.get_state(ca_val), st_or_val = st_or,
		ct_or_list = sof.get_city(ca_val,st_or), ct_or_val = city_or,
		ae_or_list = sof.get_aero(ca_val,st_or,city_or), ae_or_val = aero_or,
		date_or_val = date_or, time_or_val = time_or,
		st_ar_list = sof.get_state_dest(ca_val), st_ar_val = st_ar,
		ct_ar_list = sof.get_city_dest(ca_val,st_ar), ct_ar_val = city_ar,
		ae_ar_list = sof.get_aero_dest(ca_val,st_ar,city_ar), ae_ar_val = aero_ar,
		date_ar_val = date_ar, time_ar_val = time_ar, 
		dt_not_valide = dt_not_valide)  

@app.route('/pred/', methods=['GET', 'POST'])
def pred():

	ca_val = request.form['ca']
	step = int(request.form['step'])
	st_or = request.form['st_or']
	city_or = request.form['ct_or']
	aero_or = request.form['ae_or']
	date_or = request.form['date_or']
	time_or = request.form['time_or']
	st_ar = request.form['st_ar']
	city_ar = request.form['ct_ar']
	aero_ar = request.form['ae_ar']
	date_ar = request.form['date_ar']
	time_ar = request.form['time_ar']

	dataf = creat_dataframe(app.config['STRUCT'])
	dataf = fill_df(dataf,app.config['DH'] , ca_val, city_or, aero_or, date_or, time_or, city_ar, aero_ar, time_ar)

	retard = 3

	return render_template('pred.html', ca_val = COMP_AER[ca_val], ct_or_val = city_or , ae_or_val = aero_or, date_or_val = date_or, time_or_val = time_or, 
		ct_ar_val = city_ar, ae_ar_val = aero_ar, date_ar_val = date_ar, time_ar_val = time_ar, retard = retard) 