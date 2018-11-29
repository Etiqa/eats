from setuptools import setup, find_packages

from eats.__version__ import __version__

setup(
    name='etiqa-eats',
    version=__version__,
    url='https://github.com/Etiqa/eats',
    license='2-clause BSD License',
    author='Fabio Pulvirenti',
    author_email='fabio@etiqa.it',
    packages=find_packages(exclude=['*tests*']),
    package_data={'eats.utils': ['scripts/*.js'],
                  'eats.webdriver': ['scripts/*.js']
                  },
    description='Easy Automation Testing Selenium',
    long_description='EATS is obsolete and no longer maintained: please consider using Bromine (https://github.com/Etiqa/bromine)',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7'
    ],
    install_requires=[
        "selenium ~= 3.6",
        "etiqa-pytractor == 0.2.1.1",
        "etiqa-behave == 1.2.6.0",
        "pyhamcrest == 1.8.5",
        "beautifulsoup4",
        "Pillow",
        "Appium-Python-Client == 0.26",
        "lxml",
        "junit2html"
    ],
    extras_require={
        'dev': [
            'unittest-xml-reporting'
        ]
    }

)


# external dependency: lxml
#  -> on MACOSX El Capitan: `STATIC_DEPS=true pip install lxml`
