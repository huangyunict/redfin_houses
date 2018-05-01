from distutils.core import setup
import setuptools

setup(
    name='redfin-houses',
    version='0.0.1',
    packages=['redfin_houses'],
    author='Yun Huang',
    author_email='huangyunict@gmail.com',
    description='Python library to retrieve house information from Redfin.',
    url='https://github.com/huangyunict/redfin_houses',
    download_url='https://pypi.org/project/redfin_houses/',
    keywords='redfin house real estate'.split(),
    license='GNU LGPLv3',
    python_requires='>=3',
    install_requires=[
        "pyquery >= 1.4.0",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
