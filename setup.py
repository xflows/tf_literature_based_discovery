import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='tf_literature_based_discovery',
    version='0.0.6',
    packages=['tf_literature_based_discovery'],
    include_package_data=True,
    license='MIT License',
    description='TextFlows module for literature-based cross-context discovery',
    long_description=README,
    url='https://github.com/xflows/tf_literature_based_discovery',
    author='Matic Perovsek',
    author_email='matic.perovsek@ijs.si',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        "tf_core",
        #"tf_latino", required only for explore in crossbee widget
    ]
)
