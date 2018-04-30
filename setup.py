from distutils.core import setup
import setuptools

setup(
    name='redfin_houses',
    version='0.0.1',
    packages=['redfin_houses'],
    author='Yun Huang',
    author_email='huangyunict@gmail.com',
    description='Retrieves house information from redfin.com',
    url='https://github.com/huangyunict/redfin_houses',
    download_url='http://pypi.python.org/pypi/redfin_houses',
    keywords='redfin house'.split(),
    license='GNU LGPLv2+',
    install_requires=[
        "beautifulsoup4 >= 4.2.1",
        "pyquery >= 1.4.0",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
    	'Natural Language :: English',
    	'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
