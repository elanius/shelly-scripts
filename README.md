# Shelly Scripts

## Overview
Shelly Scripts is a Python module for interacting with Shelly smart home devices. It includes scripts to automate and control Shelly devices via their API.

## Installation
To install the scripts, clone the repository and install the dependencies:
```
git clone git@github.com:elanius/shelly-scripts.git
cd shelly_scripts
```
Create virtual env and activate it
```
virtualenv -p python3.10 venv
source venv/bin/activate
pip install -e ./
```

## Usage
The module contains scripts like `shelly_commands.py` which can be run with specific arguments to control Shelly devices.

Example:
```
python shelly_scripts/shelly_commands.py --ip <Shelly device IP> --commands <JSON command file>
```

## Features
- Control Shelly devices via HTTP RPC calls
- Schedule device actions
- Toggle device switches
