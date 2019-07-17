#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
#title           :pyrofilegen.py
#description     :pyrofilegen is a python-based realistic Canadian data generator.
#author          :Tejinder Purba
#date            :July 10, 2019
#version         :0.1
#==============================================================================

This module allows for the creation of realistic linked Canadian data
with the option for variation to occur for realistic bulk datasets and
various other data output formats.

Data that can be generated includes: 
	-First Name
	-Last Name
	-Date of Birth
	-Height
	-Weight
	-Address (Street Number, Street Name, City, Province, Postal Code, Lat-Long)
	-Credit Card (Number, Expiry, CVV, Pin)
	-Email
	-Password
	-Phone Number
	-SIN
	-Driver's License
	-License Plate
	-Company
	-User Agent
	-Astrological Sign

Attributes:
	parent_path (str): File path of the parent directory for where the 
		program is being run. 
	assets_path (str): File path of the assets directory based on where the 
		program is being run.
	canadian_data_file_name (str): File path & name of the main canadian_data.csv
		file name.
	canadian_area_codes_file_name (str): File path & name of the 
		canadian_area_codes.txt file name.
	canadian_companies_file_name (str): File path & name of the main 
		canadian_companies.txt file name.
	province_list (list): List containing each province/territory in Canada.
	faker (module): Module containing the initialization of the Faker library.
	gender (str): Global variable to hold the gender of the current profile
"""

import time
import datetime
import sys
import os
from os.path import dirname
import random
import string
from faker import Faker
import csv

parent_path = dirname(dirname(os.path.abspath(__file__)))                               # Configure parent directory    
assets_path = parent_path+'/assets/'                                                    # Configure assets directory                                             

# Data Paths
#==============================================================================
canadian_data_file_name = os.path.join(assets_path, 'canadian_data.csv') 
canadian_area_codes_file_name = os.path.join(assets_path, 'canadian_area_codes.txt') 
canadian_companies_file_name = os.path.join(assets_path, 'canadian_companies.txt') 
province_list = ["ontario", "quebec", "british columbia", "alberta", "manitoba", "saskatchewan", "nova scotia", "new brunswick", "newfoundland and labrador", 
				 "prince edward island", "northwest territories", "nunavut", "yukon"]
#==============================================================================

faker = Faker()
gender = None

def generate_first_name(chance=None, variation=False):
	"""
	Function to generate the first name of the profile based on gender.

	Args:
		chance: Integer between 1-100 used for the variation option. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)

	Returns:
		The return value. String value containing profile first name.

	"""
	global gender
	if not chance:
		chance = random.randint(1, 100)
	if chance >= 50:
		gender = 'Male'
		first_name = str(faker.first_name_male())
		if variation:
			if chance <= 25:
				pass
			elif chance > 25 and chance <= 50:
				gender = gender.upper()
				first_name = first_name.upper()
			else:
				gender = gender.lower()
				first_name = first_name.lower()
		return first_name
	else:
		gender = 'Female'
		first_name = str(faker.first_name_female())
		if variation:
			if chance <= 25:
				pass
			elif chance > 25 and chance <= 50:
				gender = gender.upper()
				first_name = first_name.upper()
			else:
				gender = gender.lower()
				first_name = first_name.lower()
		return first_name

def generate_last_name(chance=None, variation=False):
	"""
	Function to generate the last name of the profile.

	Args:
		chance: Integer between 1-100 used for the variation option. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)

	Returns:
		The return value. String value containing profile last name.

	"""
	if not chance:
		chance = random.randint(1,100)
	last_name = str(faker.last_name())
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			last_name = last_name.upper()
		else:
			last_name = last_name.lower()
	return last_name

def generate_dob_year():
	"""
	Function to generate the year for date of birth of the profile.

	Returns:
		The return value. String value containing year for date of birth.

	"""
	return str("%02d" % random.randint(1950,1996))

def generate_dob_month():
	"""
	Function to generate the month for date of birth of the profile.

	Returns:
		The return value. String value containing month for date of birth.

	"""
	return str("%02d" % random.randint(1,12))

def generate_dob_day():
	"""
	Function to generate the day for date of birth of the profile.

	Returns:
		The return value. String value containing day for date of birth.

	"""
	return str("%02d" % random.randint(2,27))

def generate_dob_full(format="mmddyyyy"):
	"""
	Function to generate the date of birth of the profile.

	Args:
		format: String value used to indicate required format. (optional)
			Options include: 
			-yyyy-mm-dd
			-yyyy-dd-mm
			-dd-mm-yyyy
			-mm-dd-yyyy
			-yyyy/mm/dd
			-yyyy/dd/mm
			-dd/mm/yyyy
			-mm/dd/yyyy
			-yyyymmdd
			-yyyyddmm
			-ddmmyyyy
			-mmddyyyy

	Returns:
		The return value. String value containing date of birth.

	"""
	if format.lower() == "yyyy-mm-dd":
		return "%s-%s-%s" % (dob_year(),dob_month(),dob_day())
	elif format.lower() == "yyyy-dd-mm":
		return "%s-%s-%s" % (dob_year(),dob_day(),dob_month())
	elif format.lower() == "dd-mm-yyyy":
		return "%s-%s-%s" % (dob_day(),dob_month(),dob_year())
	elif format.lower() == "mm-dd-yyyy":
		return "%s-%s-%s" % (dob_month(),dob_day(),dob_year())
	elif format.lower() == "yyyy/mm/dd":
		return "%s/%s/%s" % (dob_year(),dob_month(),dob_day())
	elif format.lower() == "yyyy/dd/mm":
		return "%s/%s/%s" % (dob_year(),dob_day(),dob_month())
	elif format.lower() == "dd/mm/yyyy":
		return "%s/%s/%s" % (dob_day(),dob_month(),dob_year())
	elif format.lower() == "mm/dd/yyyy":
		return "%s/%s/%s" % (dob_month(),dob_day(),dob_year())
	elif format.lower() == "yyyymmdd":
		return "%s%s%s" % (dob_year(),dob_month(),dob_day())
	elif format.lower() == "yyyyddmm":
		return "%s%s%s" % (dob_year(),dob_day(),dob_month())
	elif format.lower() == "ddmmyyyy" or format == None:
		return "%s%s%s" % (dob_day(),dob_month(),dob_year())
	elif format.lower() == "mmddyyyy":
		return "%s%s%s" % (dob_month(),dob_day(),dob_year())
	else:
		return "%s%s%s" % (dob_day(),dob_month(),dob_year())

def generate_credit_card(card_type=None):
	"""
	Function to generate the credit card number of the profile.

	Args:
		card_type: String value, either "Visa" or "Mastercard". (optional)

	Returns:
		The return value. String value containing credit card number.

	"""
	if not card_type:
		card_type = random.choice(['VISA', 'Mastercard'])
	if card_type.lower() == "visa":
		return '4'+str(random.randint(123242323223432,986879876876876))
	elif card_type.lower() == "mastercard":
		return '5'+str(random.randint(123242323223432,986879876876876))

def generate_cvv():
	"""
	Function to generate the cvv of the profile.

	Returns:
		The return value. String value containing credit card cvv.

	"""
	return str(random.randint(124,965))

def generate_card_expiry_month():
	"""
	Function to generate the credit card expiry month of the profile.

	Returns:
		The return value. String value containing credit card expiry month.

	"""
	return str("%02d" % random.randint(1,12))

def generate_card_expiry_year():
	"""
	Function to generate the credit card expiry year of the profile.

	Returns:
		The return value. String value containing credit card expiry year.

	"""
	now = datetime.datetime.now()
	earliest_year = now.year+2-2000
	latest_year = now.year+4-2000
	return str(random.randint(earliest_year,latest_year))

def generate_card_expiry(format="mm/yy"):
	"""
	Function to generate the credit card expiry of the profile.
	
	Args:
		format: String value used to indicate required format. (optional)
			Options include: 
			-mm/yy
			-mm-yy
			-mmyy
			
	Returns:
		The return value. String value containing credit card expiry.

	"""
	if format == "mm/yy":
		return "%s/%s" % (generate_card_expiry_month(), generate_card_expiry_year())
	elif format == "mm-yy":
		return "%s-%s" % (generate_card_expiry_month(), generate_card_expiry_year())
	elif format == "mmyy":
		return "%s%s" % (generate_card_expiry_month(), generate_card_expiry_year())
	else:
		return None

def generate_card_pin():
	"""
	Function to generate the credit card pin of the profile.

	Returns:
		The return value. String value containing credit card pin.

	"""
	return str(random.randint(1123,9850))

def generate_password(chance=None, first_name=None, last_name=None, dob_year=None, dob_month=None, dob_day=None):
	"""
	Function to generate the password of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		first_name: String value for the first name of profile (optional)
		last_name: String value for the last name of profile (optional)
		dob_year: String value for the date of birth year of profile (optional)
		dob_month: String value for the date of birth month of profile (optional)
		dob_day: String value for the date of birth day of profile (optional)
			
	Returns:
		The return value. String value containing the password.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not first_name or chance > 75:
		first_name_choices = ["god", "love", "lust", "money", "private", "qwerty", "secret", "snoopy", "disney", "kitty"]
		first_name = str(random.choice(first_name_choices))
	if not last_name:
		last_name_choices = ["football", "hockey", "piano", "burger", "food", "password", "mushy", "nose", "dark", "doggy"]
		last_name = str(random.choice(last_name_choices))
	if not dob_year:
		dob_year = generate_dob_year()
	if not dob_month:
		dob_month = generate_dob_month()
	if not dob_day:
		dob_day = generate_dob_day()
	password_choices = ["%s.%s%s" % (first_name[0], last_name,dob_year[2:]), "%s%s%s" % (last_name,dob_month,dob_day), "%s.%s%s" % (last_name[0], first_name, dob_year), "%s%s%s" % (last_name, first_name, str(random.randint(2002,2016))), "%s.%s%s" % (first_name, last_name, str(random.randint(20,99))), "%s_%s%s" % (first_name, last_name,dob_year[2:]), "%s_%s%s" % (last_name, first_name, dob_year),"%s%s%s" % (first_name, last_name, dob_year[2:]), "%s%s" %(last_name, str(random.randint(0,9999)))]
	password = str(random.choice(password_choices)).lower()
	if chance <= 25:
		pass
	elif chance > 25 and chance <= 50:
		password = string.capwords(password)
	elif chance > 50 and chance <= 75:
		password = password+"!"
	else:
		password = string.capwords(password)
		password = password+"!"
	return password

def generate_sin(province=None):
	"""
	Function to generate the SIN of the profile.

	Args:
		province: String value containing province of choice for SIN formatting. (optional)

	Returns:
		The return value. String value containing the SIN.

	"""
	if not province:
		province = str(random.choice(province_list))
	else:
		province = province.lower()
	if province == "nova scotia" or province == "new brunswick" or province == "prince edward island" or province == "newfoundland and labrador": 
		return str(random.randint(112345690,198876546))
	elif province == "quebec":
		return str(random.randint(212345690,398876546))
	elif province == "ontario":
		return str(random.randint(412345690,598876546))
	elif province == "manitoba" or province == "saskatchewan" or province == "alberta" or province == "northwest territories" or province == "nunavut":
		return str(random.randint(612345690,698876546))
	elif province == "british columbia" or province == "yukon":
		return str(random.randint(712345690,798876546))
	else:
		return str(random.randint(112345690,798876546))

def generate_drivers_license(province=None, first_name=None, last_name=None, dob_year=None, dob_month=None, dob_day=None):
	"""
	Function to generate the driver's license of the profile.
	
	Args:
		province: String value containing province of choice for SIN formatting. (optional)
		first_name: String value for the first name of profile (optional)
		last_name: String value for the last name of profile (optional)
		dob_year: String value for the date of birth year of profile (optional)
		dob_month: String value for the date of birth month of profile (optional)
		dob_day: String value for the date of birth day of profile (optional)
			
	Returns:
		The return value. String value containing the driver's license.

	"""
	if not province:
		province = str(random.choice(province_list))
	if not first_name:
		first_name = generate_first_name()
	if not last_name:
		last_name = generate_last_name()
	if not dob_year:
		dob_year = generate_dob_year()
	if not dob_month:
		dob_month = generate_dob_month()
	if not dob_day:
		dob_day = generate_dob_day()
	province = str(province).lower()
	if province == "newfoundland and labrador" or province == "nl":
		return "%s%s%s%s%s" % (last_name[0].upper(),dob_year[2:],dob_month,dob_day,str(random.randint(124,965)))
	elif province == "new brunswick" or province == "nb":
		return str(random.randint(1240303,9659478))
	elif province == "nova scotia" or province == "ns":
		return "%s%s%s%s%s" % (last_name[:5].upper(),dob_day,dob_month,dob_year[:2],str(random.randint(124,965))) 
	elif province == "prince edward island" or province_list == "pe":
		return "%s%s%s%s%s" % (str(random.randint(1240,9650)),dob_day,dob_month,dob_year[:2],str(random.randint(12,96))) 
	elif province == "quebec" or province == "qc":
		return "%s%s%s%s%s%s" % (last_name[0].upper(),str(random.randint(1240,9650)),dob_day,dob_month,dob_year[2:],str(random.randint(12,96)))
	elif province == "ontario" or province == "on":
		return "%s%s%s%s%s" % (last_name[0].upper(),str(random.randint(12402345,96503647)),dob_year[2:],dob_month,dob_day)
	elif province == "alberta" or province == "saskatchewan" or province == "ab" or province == "sk":
		return str(random.randint(21234569,99887654))
	elif province == "manitoba" or province == "mb":
		letters = string.ascii_uppercase
		return "%s%s" % (''.join(random.choice(letters) for i in range(7)),str(random.randint(11245,94276)))
	elif province == "northwest territories" or province == "nunavut" or province == "nt" or province == "nu":
		return str(random.randint(112450,942769))
	elif province == "british columbia" or province == "bc":
		return str(random.randint(2123456,9988765))
	elif province == "yukon" or province == "yk":
		return str(random.randint(212345,998876))
	else:
		return None

def generate_email(chance=None, first_name=None, last_name=None, dob_year=None, dob_month=None, dob_day=None):
	"""
	Function to generate the email of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		first_name: String value for the first name of profile (optional)
		last_name: String value for the last name of profile (optional)
		dob_year: String value for the date of birth year of profile (optional)
		dob_month: String value for the date of birth month of profile (optional)
		dob_day: String value for the date of birth day of profile (optional)
			
	Returns:
		The return value. String value containing the email.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not first_name:
		first_name = generate_first_name()
	if not last_name:
		last_name = generate_last_name()
	if not dob_year:
		dob_year = generate_dob_year()
	if not dob_month:
		dob_month = generate_dob_month()
	if not dob_day:
		dob_day = generate_dob_day()
	email_choices = ["%s.%s%s" % (last_name[0], first_name, dob_year), "%s%s%s" % (last_name, first_name, str(random.randint(2002,2016))), "%s.%s%s" % (first_name, last_name, str(random.randint(20,99))), "%s_%s%s" % (first_name, last_name,dob_year[2:]), "%s_%s%s" % (last_name, first_name, dob_year),"%s%s%s" % (first_name, last_name, dob_year[2:]), "%s%s" %(last_name, str(random.randint(0,9999)))]
	email = str(random.choice(email_choices)).lower()
	if chance <= 35:  
		return email + "@hotmail.com"
	elif chance > 35 and chance <= 50:
		return email + "@yahoo.com"
	else:
		return email + "@gmail.com"

def generate_phone_number(location=None, format=5):
	"""
	Function to generate the phone number of the profile.
	
	Args:
		location: List containing string values for city and/or province. (optional)
		format: String value used to indicate required format. (optional)
			Options include: 
			-1 (xxxxxxxxxxx)
			-2 (xxx xxx xxxx)
			-3 (xxx-xxx-xxxx)
			-4 ((xxx)xxxxxxx)
			-5 ((xxx) xxx xxxx)
			-6 ((xxx)-xxx-xxxx)

	Returns:
		The return value. String value containing the phone number.

	"""
	area_code_dict = eval(open(canadian_area_codes_file_name).read())
	area_code = None
	if location:
		if isinstance(location, str):
			location = [location]
		for x in location:
			if x.lower() in area_code_dict:
				area_code = str(area_code_dict[x.lower()])
				break
		if not area_code:
			return None
	else:
		key = random.choice(list(area_code_dict.keys()))
		area_code = str(area_code_dict[key])  
	if format == 1 or format == "1":
		return "%s%s" % (area_code,str(random.randint(1203948,9467868)))
	elif format == 2 or format == "2":
		return "%s %s %s" % (area_code,str(random.randint(120,946)),str(random.randint(1200,9460)))
	elif format == 3 or format == "3":
		return "%s-%s-%s" % (area_code,str(random.randint(120,946)),str(random.randint(1201,9460)))
	elif format == 4 or format == "4":
		return "(%s)%s" % (area_code,str(random.randint(1203948,9467868)))
	elif format == 5 or format == "5":
		return "(%s) %s %s" % (area_code,str(random.randint(120,946)),str(random.randint(1200,9460)))
	elif format == 6 or format == "6":
		return "(%s)-%s-%s" % (area_code,str(random.randint(120,946)),str(random.randint(1200,9460)))

def generate_street_number(row=None):
	"""
	Function to generate the street number of the profile.
	
	Args:
		row: Comma delimited row from canadian_data.csv. (not required)

	Returns:
		The return value. String value containing the street number.

	"""
	if not row:
		csv_file = open(canadian_data_file_name, 'r')
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = random.choice(list(csv_reader))
		csv_file.close()
	return str(row[2])

def generate_street_name(chance=None, variation=False, row=None):
	"""
	Function to generate the street name of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)
		row: Comma delimited row from canadian_data.csv. (not required)

	Returns:
		The return value. String value containing the street name.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not row:
		csv_file = open(canadian_data_file_name, 'r')
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = random.choice(list(csv_reader))
		csv_file.close()
	temp = str(row[3]).lower()
	street_name = string.capwords(temp)
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			street_name = street_name.replace("Street", "St.")
			street_name = street_name.replace("Crescent", "Cres")
			street_name = street_name.replace("Road", "Rd")
			street_name = street_name.replace("Avenue", "Ave")
			street_name = street_name.replace("Drive", "Dr.")
			street_name = street_name.replace("Lane", "Ln")
			street_name = street_name.upper()
		elif chance > 50 and chance <= 75:
			street_name = street_name.replace("Street", "St.")
			street_name = street_name.replace("Crescent", "Cres.")
			street_name = street_name.replace("Road", "Rd.")
			street_name = street_name.replace("Avenue", "Ave.")
			street_name = street_name.replace("Drive", "Dr.")
			street_name = street_name.replace("Lane", "Ln.")
			street_name = street_name.lower()
		elif chance > 75:
			street_name = street_name.lower()
	return street_name

def generate_postal_code(chance=None, variation=False, row=None):
	"""
	Function to generate the postal code of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)
		row: Comma delimited row from canadian_data.csv. (not required)

	Returns:
		The return value. String value containing the postal code.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not row:
		csv_file = open(canadian_data_file_name, 'r')
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = random.choice(list(csv_reader))
		csv_file.close()
	postal_code = str(row[6])
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			postal_code = postal_code.upper()
		else:
			postal_code = postal_code.lower()
	return postal_code

def generate_city(chance=None, variation=False, row=None):
	"""
	Function to generate the city of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)
		row: Comma delimited row from canadian_data.csv. (not required)

	Returns:
		The return value. String value containing the city.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not row:
		csv_file = open(canadian_data_file_name, 'r')
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = random.choice(list(csv_reader))
		csv_file.close()
	city = str(row[4])
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			city = city.upper()
		else:
			city = city.lower()
	return city

def generate_province(chance=None, variation=False, row=None):
	"""
	Function to generate the province of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)
		row: Comma delimited row from canadian_data.csv. (not required)

	Returns:
		The return value. String value containing the province.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not row:
		province = random.choice(province_list)
		province = string.capwords(province)
	else:
		province = str(row[5])
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			province = province.upper()
		else:
			province = province.lower()
	return province

def generate_lat_long(format=1, row=None):
	"""
	Function to generate the lat-long coordinates of the profile.
	
	Args:
		format: String value used to indicate required format. (optional)
			Options include: 
			-1 (Str value)
			-2 (List value)
		row: Comma delimited row from canadian_data.csv. (not required)

	Returns:
		The return value. String/List value containing the lat-long coordinates.

	"""
	if not row:
		csv_file = open(canadian_data_file_name, 'r')
		csv_reader = csv.reader(csv_file, delimiter=',')
		row = random.choice(list(csv_reader))
		csv_file.close()
	lat_long = str(row[0]+","+row[1])
	if format == 1 or format == "1":
		return lat_long
	elif format == 2 or format == "2":
		lat_long_list = []
		lat_long_list.append(str(row[0]))
		lat_long_list.append(str(row[1]))
		return lat_long_list
	else:
		return None

def generate_address_full(chance=None, variation=False, format=1):
	"""
	Function to generate the full address of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)
		format: String value used to indicate required format. (optional)
			Options include: 
			-1 (Str value)
			-2 (List value)

	Returns:
		The return value. String/List value containing the full address.

	"""
	if not chance:
		chance = random.randint(1,100)
	csv_file = open(canadian_data_file_name, 'r')
	csv_reader = csv.reader(csv_file, delimiter=',')
	random_row = random.choice(list(csv_reader))
	csv_file.close()
	if format == 1 or format == "1":
		return "%s %s, %s, %s, %s" % (generate_street_number(row=random_row),generate_street_name(chance=chance, variation=variation,row=random_row),generate_city(chance=chance, variation=variation,row=random_row),generate_province(chance=chance, variation=variation,row=random_row),generate_postal_code(chance=chance, variation=variation,row=random_row))
	elif format == 2 or format == "2":
		address_list=[]
		address_list.append(generate_street_number(row=random_row))
		address_list.append(generate_street_name(variation,row=random_row))
		address_list.append(generate_city(variation,row=random_row))
		address_list.append(generate_province(variation,row=random_row))
		address_list.append(generate_postal_code(variation,row=random_row))
		return address_list

def generate_address_min(chance=None, variation=False, format=1):
	"""
	Function to generate the minimum address of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)
		format: String value used to indicate required format. (optional)
			Options include: 
			-1 (Str value)
			-2 (List value)

	Returns:
		The return value. String/List value containing the minimum address.

	"""
	if not chance:
		chance = random.randint(1,100)
	csv_file = open(canadian_data_file_name, 'r')
	csv_reader = csv.reader(csv_file, delimiter=',')
	random_row = random.choice(list(csv_reader))
	csv_file.close()
	if format == 1 or format == "1":
		return "%s %s, %s" % (generate_street_number(row=random_row),generate_street_name(chance=chance, variation=variation, row=random_row),generate_postal_code(chance=chance, variation=variation, row=random_row))
	elif format == 2 or format == "2":
		address_list=[]
		address_list.append(generate_street_number(row=random_row))
		address_list.append(generate_street_name(chance=chance, variation=variation, row=random_row))
		address_list.append(generate_postal_code(chance=chance, variation=variation, row=random_row))
		return address_list

def generate_user_agent():
	"""
	Function to generate the user agent of the profile.

	Returns:
		The return value. String value containing the user agent.

	"""
	return str(faker.user_agent())

def generate_astrological_sign(chance=None, dob_month=None, dob_day=None, variation=False):
	"""
	Function to generate the astrological sign of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		dob_month: String value for the date of birth month of profile (optional)
		dob_day: String value for the date of birth day of profile (optional)
		variation: Boolean value indicating whether variation is requested. (optional)

	Returns:
		The return value. String value containing the astrological sign.

	"""
	if not chance:
		chance = random.randint(1,100)
	if not dob_month:
		dob_month = str(random.randint(1,12))
	if not dob_day:
		dob_day = str(random.randint(1,28))
	try:
		dob_month = dob_month.lower()
	except:
		pass
	if dob_month == 'december' or dob_month == 'dec' or dob_month == '12' or dob_month == 12:
		astro_sign = 'Sagittarius' if (dob_day < 22) else 'Capricorn'
	elif dob_month == 'january' or dob_month == 'jan' or dob_month == '1' or dob_month == '01' or dob_month == 1:
		astro_sign = 'Capricorn' if (dob_day < 20) else 'Aquarius'
	elif dob_month == 'february' or dob_month == 'feb' or dob_month == '2' or dob_month == '02' or dob_month == 2:
		astro_sign = 'Aquarius' if (dob_day < 19) else 'Pisces'
	elif dob_month == 'march' or dob_month == 'mar' or dob_month == '3' or dob_month == '03' or dob_month == 3:
		astro_sign = 'Pisces' if (dob_day < 21) else 'Aries'
	elif dob_month == 'april' or dob_month == 'apr' or dob_month == '4' or dob_month == '04' or dob_month == 4:
		astro_sign = 'Aries' if (dob_day < 20) else 'Taurus'
	elif dob_month == 'may' or dob_month == '5' or dob_month == '05' or dob_month == 5:
		astro_sign = 'Taurus' if (dob_day< 21) else 'Gemini'
	elif dob_month == 'june' or dob_month == 'jun' or dob_month == '6' or dob_month == '06' or dob_month == 6:
		astro_sign = 'Gemini' if (dob_day < 21) else 'Cancer'
	elif dob_month == 'july' or dob_month == 'jul' or dob_month == '7' or dob_month == '07' or dob_month == 7:
		astro_sign = 'Cancer' if (dob_day < 23) else 'Leo'
	elif dob_month == 'august' or dob_month == 'aug' or dob_month == '8' or dob_month == '08' or dob_month == 8:
		astro_sign = 'Leo' if (dob_day < 23) else 'Virgo'
	elif dob_month == 'september' or dob_month == 'sept' or dob_month == '9' or dob_month == '09' or dob_month == 9:
		astro_sign = 'Virgo' if (dob_day < 23) else 'Libra'
	elif dob_month == 'october' or dob_month == 'oct' or dob_month == '10' or dob_month == 10:
		astro_sign = 'Libra' if (dob_day < 23) else 'Scorpio'
	elif dob_month == 'november' or dob_month == 'nov' or dob_month == '11' or dob_month == 11:
		astro_sign = 'Scorpio' if (dob_day < 22) else 'Sagittarius'
	else:
		return None
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			astro_sign = astro_sign.upper()
		else:
			astro_sign = astro_sign.lower()
	return str(astro_sign)

def generate_license_plate(province=None):
	"""
	Function to generate the license plate of the profile.
	
	Args:
		province: String value containing province of choice for plate formatting. (optional)

	Returns:
		The return value. String value containing the license plate.

	"""
	letters = string.ascii_uppercase
	if not province:
		province = str(random.choice(province_list))
	province = str(province).lower()
	if province == "newfoundland and labrador" or province == "nl" or province == "new brunswick" or province == "nb" or province == "manitoba" or province == "mb" or province == "nova scotia" or province == "ns":
		return "%s %s" % (''.join(random.choice(letters) for i in range(3)),str(random.randint(112,942)))
	elif province == "prince edward island" or province_list == "pe":
		return "%s %s%s" % (str(random.randint(12,96)),str(random.randint(1,9)),''.join(random.choice(letters) for i in range(2))) 
	elif province == "quebec" or province == "qc":
		return "%s%s %s" % (''.join(random.choice(letters) for i in range(1)), str(random.randint(11,97)), ''.join(random.choice(letters) for i in range(3)))
	elif province == "ontario" or province == "on":
		return "%s %s" % (''.join(random.choice(letters) for i in range(4)), str(random.randint(110,970)))
	elif province == "alberta" or province == "ab":
		return "%s-%s" % (''.join(random.choice(letters) for i in range(3)), str(random.randint(1102,9709)))
	elif province == "saskatchewan" or province == "sk":
		return "%s %s" % (str(random.randint(112,942)), ''.join(random.choice(letters) for i in range(3)))
	elif province == "northwest territories" or province == "nt":
		return str(random.randint(112450,942769))
	elif province == "nunavut" or province == "nu":
		return "%s %s" % (str(random.randint(112,942)), str(random.randint(112,942)))
	elif province == "british columbia" or province == "bc":
		return "%s%s %s%s" % (''.join(random.choice(letters) for i in range(2)), str(random.randint(1,9)), str(random.randint(11,97)), ''.join(random.choice(letters) for i in range(1)))
	elif province == "yukon" or province == "yk":
		return "%s%s" % (''.join(random.choice(letters) for i in range(3)), str(random.randint(11,97)))
	else:
		return None

def generate_sentence():
	"""
	Function to generate a random sentence of the profile.

	Returns:
		The return value. String value containing the sentence.

	"""
	return str(faker.sentence())

def generate_company(chance=None, variation=False):
	"""
	Function to generate the company of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)
		variation: Boolean value indicating whether variation is requested. (optional)

	Returns:
		The return value. String value containing the company.

	"""
	if not chance:
		chance = random.randint(1,100)
	canadian_companies_file = open(canadian_companies_file_name, 'r+')                                       
	canadian_companies_list = canadian_companies_file.read().split('\n') 
	canadian_companies_list = list(filter(None, canadian_companies_list))
	canadian_companies_file.close()
	company = random.choice(canadian_companies_list)
	if variation:
		if chance <= 25:
			pass
		elif chance > 25 and chance <= 50:
			company = company.upper()
		else:
			company = company.lower()
	return company

def generate_height(chance=None):
	"""
	Function to generate the height of the profile.
	
	Args:
		chance: Integer between 1-100 used for realistic variation. (not required)

	Returns:
		The return value. String value containing the height.

	"""
	if not chance:
		chance = random.randint(1,100)
	global gender
	if gender.lower() == "male":
		if chance > 85:
			return "6'"+str(random.randint(0,4))
		else:
			return "5'"+str(random.randint(7,11))
	elif gender.lower() == "female":
		return "5'"+str(random.randint(2,7))

def generate_weight():
	"""
	Function to generate the weight of the profile.

	Returns:
		The return value. String value containing the weight.

	"""
	global gender
	if gender.lower() == "male":
		return str(random.randint(160,230))+" lbs"
	elif gender.lower() == "female":
		return str(random.randint(115,160))+" lbs"

def generate_profile(format=1, variation=False, phone_num_format=5, card_expiry_format="mm/yy"):
	"""
	Function to generate the profile.
	
	Args:
		format: String value used to indicate required format. (optional)
			Options include: 
			-1 (Str value)
			-2 (List value)
			-3 (Dict value)
		variation: Boolean value indicating whether variation is requested. (optional)
		phone_num_format: See help(generate_phone_number).
		card_expiry_format: See help(generate_card_expiry).

	Returns:
		The return value. String/List/Dict value containing the profile.

	"""
	chance = random.randint(1,100)
	csv_file = open(canadian_data_file_name, 'r')
	csv_reader = csv.reader(csv_file, delimiter=',')
	row = random.choice(list(csv_reader))
	csv_file.close()
	first_name = str(generate_first_name(chance=chance, variation=variation))
	last_name = str(generate_last_name(chance=chance, variation=variation))
	mmm = str(generate_last_name(chance=chance, variation=variation))
	dob_year = str(generate_dob_year())
	dob_month = str(generate_dob_month())
	dob_day = str(generate_dob_day())
	height = generate_height(chance=chance)
	weight = generate_weight()
	address_full = generate_address_full(chance=chance, format=2, variation=variation)
	lat_long = str(generate_lat_long())
	credit_card = str(generate_credit_card())
	credit_card_expiry = str(generate_card_expiry(format=card_expiry_format))
	credit_card_cvv = str(generate_cvv())
	credit_card_pin = str(generate_card_pin())
	email = str(generate_email(first_name=first_name, last_name=last_name, dob_year=dob_year, dob_month=dob_month, dob_day=dob_day))
	password = str(generate_password(first_name=first_name, last_name=last_name, dob_year=dob_year, dob_month=dob_month, dob_day=dob_day))
	phone_num = str(generate_phone_number(location=[str(address_full[2]),str(address_full[3])], format=phone_num_format))
	sin = str(generate_sin(province=str(address_full[3])))
	drivers = str(generate_drivers_license(province=str(address_full[3]), first_name=first_name, last_name=last_name, dob_year=dob_year, dob_month=dob_month, dob_day=dob_day))
	license_plate = str(generate_license_plate(province=str(address_full[3])))
	company = str(generate_company(chance=chance, variation=variation))
	astrological_sign = generate_astrological_sign(chance=chance, dob_month=dob_month, dob_day=dob_day, variation=variation)
	if format == 1 or format == "1":
		return "Gender: %s\nFirst Name: %s\nLast Name: %s\nMother's Maiden Name: %s\nDate of Birth: %s-%s-%s\nHeight: %s\nWeight: %s\nStreet Number: %s\nStreet Name: %s\nCity: %s\nProvince: %s\nPostal Code: %s\nLat-Long: %s\nCredit Card: %s\nCredit Card Expiry: %s\nCredit Card CVV: %s\nCredit Card PIN: %s\nEmail: %s\nPassword: %s\nPhone Number: %s\nSIN: %s\nDriver's License: %s\nLicense Plate: %s\nCompany: %s\nAstrological Sign: %s" % (gender, first_name,last_name,mmm,dob_day,dob_month,dob_year,height,weight,str(address_full[0]),str(address_full[1]),str(address_full[2]),str(address_full[3]),str(address_full[4]),lat_long,credit_card,credit_card_expiry,credit_card_cvv,credit_card_pin,email,password,phone_num,sin,drivers,license_plate,company,astrological_sign)
	elif format == 2 or format == "2":
		profile_list=[]
		profile_list.extend((gender,first_name,last_name,mmm,dob_year,dob_month,dob_day,str("%s-%s-%s" % (dob_day,dob_month,dob_year)),height,weight,address_full[0],address_full[1],address_full[2],address_full[3],address_full[4],lat_long,credit_card,credit_card_expiry,credit_card_cvv,credit_card_pin,email,password,phone_num,sin,drivers,license_plate,company))
		return profile_list
	elif format == 3 or format == "3":
		profile_dict={'gender':gender, 'first_name':first_name, 'last_name':last_name, 'maiden_name':maiden_name, 'dob_year':dob_year, 'dob_month':dob_month, 'dob_day':dob_day, 'dob_full':str("%s-%s-%s" % (dob_day,dob_month,dob_year)), 'height':height, 'weight':weight, 'street_num':address_full[0], 'street_name':address_full[1], 'city':address_full[2], 'province':address_full[3], 'postal_code':address_full[4], 'lat_long':lat_long, 'credit_card':credit_card, 'credit_card_expiry':credit_card_expiry, 'credit_card_cvv':credit_card_cvv, 'credit_card_pin':credit_card_pin, 'email':email, 'password':password, 'phone_num':phone_num, 'sin':sin, 'drivers_license':drivers, 'license_plate':license_plate, 'company':company, 'astrological_sign':astrological_sign}
		return profile_dict