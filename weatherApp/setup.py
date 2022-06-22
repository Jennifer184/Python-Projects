# setup.py
from setuptools import setup

setup(
    name='weatherApp',
    version='0.1.0',
    description='A weather application that reads the temp',
    url='https://github.com/Jennifer184/Python-Projects',
    author='Jennifer184',
    author_email='',
    license='BSD 2-clause',
    packages=['weatherApp'],
    install_requires=['gtts',
                      'BeautifulSoup4'
                      ],
     classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: Microsoft :: Windows',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9',

    ],
)