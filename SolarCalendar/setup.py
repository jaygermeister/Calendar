from setuptools import setup, find_packages

setup(
    name="solar-calendar",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "astropy>=5.0.0",
        "ephem>=4.1.0",
        "pytz>=2021.3",
        "python-dateutil>=2.8.2",
    ],
    entry_points={
        "console_scripts": [
            "solar-calendar=solar_calendar.menu:main",
        ],
    },
) 