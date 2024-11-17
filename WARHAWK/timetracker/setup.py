from setuptools import setup, find_packages

setup(
    name="timetracker",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
    entry_points={
        'console_scripts': [
            'timetracker=timetracker.cli:main',  
        ],
    },
    author="Satyam",
    description="A CLI Program that tracks time",
)