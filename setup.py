#!/usr/bin/env python

from setuptools import setup

#twiimote basic setup.

#to run be able to run twiimote, 
#you need python-cwiid & python-bluetooth.

setup(name='twiimote',
      version='1.7',
      packages=['twiimote',],
      include_package_data=True,
      description='a wiimote to twitter thingy.',
      author='Wesley Hill',
      author_email='wesley@hakobaito.co.uk',
      license='MIT License',
      install_requires=['colorama==0.2.5','twython>=3.0.0', 'oauthlib>=0.5.0'],
      platforms=['Linux', 'Raspberry Pi'],
      long_description=open('README.txt').read(),
      url='http://hakob.yt/e/twiimote',
      classifiers=["Environment :: Console"],
      entry_points={'console_scripts':['twiimote=twiimote:main']}
     )
