from setuptools import setup, find_packages

setup(
    name='PythonFramework_Git',
    version='0.1.0',
    description='Python Test automation project',
    packages=find_packages(include=['PythonFramework_Git', 'PythonFramework_Git.*']),
    install_requires=[
        'PyYAML','atomicwrites', 'attrs', 'boto3', 'colorama', 'importlib-metadata', 'more-itertools', 'namedlist', 'openpyxl', 'packaging', 'pandas', 'pluggy', 'py', 'pyparsing', 'pytest-html', 'pytest-metadata', 'python-dateutil', 'pytz', 'requests', 's3transfer', 'selenium', 'six', 'wcwidth', 'xlrd'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
