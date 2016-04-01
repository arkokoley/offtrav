from setuptools import setup

setup(name='OffTrav', version='1.0',
      description='en',
      author='CODERS', author_email='',
      url='offtrav.localtunnel.me',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask',
                        'Flask-RESTful',
                        'MySQL-python'
      ],
     )

