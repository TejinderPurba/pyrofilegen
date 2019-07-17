# Pyrofilegen
## Installation
	pip install pyrofilegen
## Usage

################### Linked Data (String) ###################
	
	>>import pyrofilegen

	>>pyrofilegen.generate_profile()
	Gender: Male 
	First Name: Bryan 
	Last Name: Hubbard 
	Mother's Maiden Name: King
	Date of Birth: 08-05-1969<
	Height: 6'2
	Weight: 221 lbs
	Street Number: 162
	Street Name: Anvil Crescent
	City: Kamloops
	Province: British Columbia
	Postal Code: V2C 6E2
	Lat-Long: 43.7706703,-79.7500157
	Credit Card: 5689864797497581
	Credit Card Expiry: 04/22
	Credit Card CVV: 776
	Credit Card PIN: 8979
	Email: bryan_hubbard69@hotmail.com
	Password: b.hubbard69
	Phone Number: (250) 538 3205
	SIN: 746583403
	Driver's License: 3784972
	License Plate: PU3 38U
	Company: Harlequin Enterprises
	Astrological Sign: Gemini
	
################### Linked Data (List, Variation) ###################

	>>import pyrofilegen

	>>pyrofilegen.generate_profile(format=2, variation=True)

>['FEMALE', 'SARAH', 'GARNER', 'TURNER', '1951', '02', '11', '11-02-1951', "5'3", '126 lbs', '24', 'Browside Avenue', 'Toronto', 'Ontario', 'M5P 2T6', '46.5418009,-80.9053934', '5562940095183059', '03/22', '876', '5028', 'garnersarah2015@gmail.com', 'garner0211', '(416) 330 6497', '431621761', 'G85353017510211', 'XYMB 356', 'AFFINITY CREDIT UNION']

################### Unlinked Data ###################

	>>import pyrofilegen

	>>print pyrofilegen.generate_first_name(variation=True)
	>>print pyrofilegen.generate_last_name(variation=True)
	>>print pyrofilegen.generate_email()
	>>print pyrofilegen.generate_address_min(variation=True)
>Jenna
Nelson
mark.garrett33@yahoo.com
65 annala drive, p3l 1c2

################### Pseudo-Linked Data ###################

	>>import pyrofilegen

	>>f_name = pyrofilegen.generate_first_name(variation=True)
	>>l_name = pyrofilegen.generate_last_name(variation=True)
	>>dob_y = pyrofilegen.generate_dob_year()
	>>dob_m = pyrofilegen.generate_dob_month()
	>>prov = pyrofilegen.generate_province()
	>>city = pyrofilegen.generate_city()

	>>password = pyrofilegen.generate_password(first_name=f_name, last_name=l_name, dob_year=dob_y, dob_month=dob_m, dob_day=None)
	>>phone_num = pyrofilegen.generate_phone_number(location=[city,prov], format=6)
	>>print password 
	>>print phone_num

>morgan3996! 
>(905)-208-6639

	
## FAQ
### What is Pyrofilegen?

Pyrofilegen is a simple python-based application used to easily generate realistic linked pseudo-random data, typically for application testing. 

### Why did you create Pyrofilegen?

I was in the need of bulk realistic test data based only on Canadian credentials. Although other libraries like *Faker* offered a variety of data generation, even based on locales, it lacked the ability to generate linked data that would look realistic when put together in a single user profile.

From that need spawned **Pyrofilegen**, a quick way to generate thousands of realistic user profiles.

### Why should I use this package compared to others?

The reason for that would be the same reason I made this package. Although other packages offered the ability to generate pseudo-random data, the realism was lacking. The data generated was generally not linked together, i.e. the name did not match the email, and the area code of the phone number did not match the address. 

With this package, users will be able to generate realistic user profiles with real addresses, and a variety of other matching data. For example:
- Phone number based on Canadian locations (city and province, major cities only).
- Driver's license & license plate based on province and name/date of birth.
- Password based on name/date of birth.
- Variation in the generated data, meaning difference in capitalization and chance based outputs.

### What type of information does Pyrofilegen generate?

Currently the list of data that Pyrofilegen can generate is:

- First Name
- Last Name
- Date of Birth
- Height
- Weight
- Address (Street Number, Street Name, City, Province, Postal Code, Lat-Long)
- Credit Card (Number, Expiry, CVV, Pin)
- Email
- Password
- Phone Number
- SIN
- Driver's License
- License Plate
- Company
- User Agent
- Astrological Sign

### What version of python do I need?

Barnum should work on python 2.7.x and python 3.x

### How do I use it?

Refer to the **Usage** section above. 

Although this package only offers single profile generation at a time, the functions can easily be put into loops to generate huge CSVs filled with realistic, varying test data.

Simple Example:

	num_profiles_to_generate = 100
                  
	counter = 0
	while counter < num_profiles_to_generate:
	    print(str(counter))
	    with open('profiles.csv', 'a') as f:
	        prof_list = pyrofilegen.generate_profile(format=2, variation=True, phone_num_format=1)
	        data_list=[]
	        data_list.extend((prof_list[1],prof_list[2],prof_list[21],prof_list[18],pyrofilegen.generate_card_expiry_month(),pyrofilegen.generate_card_expiry_year(),prof_list[3],prof_list[4],prof_list[5],prof_list[6],prof_list[23],prof_list[24],prof_list[19],prof_list[20],prof_list[10],prof_list[11],prof_list[14],prof_list[22]))
	        writer = csv.writer(f)
	        writer.writerow(data_list)
	    f.close()
	    counter+=1

### Where does the data come from?

The address data stored in the *assets* folder are all real addresses sourced from https://openaddresses.io/.
The postal codes were then generated for each address using geopy (https://pypi.org/project/geopy/).
The names and user agents are sourced from the Faker module, which are sourced from an internal data file.
All other data is randomly generated using the *random* library.

### How can I add more data?
As this package is currently focused on Canadian data, more data can be added with ease, but only to the existing Canadian data source files. Possible data additions include:
- *canadian_data.csv* which includes the lat-long, street number, name, city, province and postal codes.
- *canadian_companies.txt* which includes a list of real Canadian companies.
- *canadian_area_codes.txt* which includes a dict of cities/provinces mapped to their area codes.


# pyrofilegen
