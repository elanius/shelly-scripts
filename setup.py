from setuptools import setup, find_packages

setup(
    name='shelly_scripts',
    version='0.1.0',
    description='Scripts to interact with Shelly devices',
    author='Stanislav Alexovic',
    author_email='stanislav.alexovic@gmail.com',
    url='https://github.com/elanius/shelly-scripts',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'shelly_commands=shelly_scripts.shelly_commands:main',
        ],
    },
)
