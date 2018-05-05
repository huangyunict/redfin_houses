from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='redfin-houses',
    version='0.0.2',
    description='Python library to retrieve house information from Redfin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/huangyunict/redfin_houses',
    author='Yun Huang',
    author_email='huangyunict@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='redfin house real estate',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    license='GNU LGPLv3',
    python_requires='>=3',
    install_requires=[
        "pyquery >= 1.4.0",
    ],
)

