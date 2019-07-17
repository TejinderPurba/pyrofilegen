from distutils.core import setup
setup(
	name = 'pyrofilegen',         
	packages = ['pyrofilegen'],   
	version = '0.1',      
	license='MIT',        
	description = 'pyrofilegen is a python-based realistic Canadian data generator.',  
	author = 'Tejinder Purba',                   
	author_email = 'rikkupurba@gmail.com',     
	url = 'https://github.com/TejinderPurba',  
	download_url = 'https://github.com/TejinderPurba/pyrofilegen/archive/0.1.tar.gz',    
	keywords = ['PROFILE', 'GENERATOR', 'REALISTIC', 'CANADIAN', 'FAKE', 'DATA'],   
	install_requires=[            
					'faker',
			],
	classifiers=[
		'Development Status :: 4 - Beta', 
		'Intended Audience :: Developers',     
		'Topic :: Software Development :: Build Tools',    
		'License :: OSI Approved :: MIT License',  
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.2',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
	],
	package_data={
        'pyrofilegen': ['assets/*.txt','assets/*.csv'],
},
)
