# primex

Prime Number Finder Server Edition
Two modes available:
1. Uses bottom and top value to calculate all prime numbers in between and outputs to csv file using python
2. Continuously calculates prime numbers of increasing magnitude with start stop functionality
Developed and maintained by @harrisongoeldner and @CountToInfinity\
Version 1.0.0 alpha (undeveloped)

## Compatibility
Tested on MacOS Big Sur (11.0.1)\
Requires Python 3 to run

## Usage
File can be run from terminal typing `python` or `python3` depending on your system configuration

## Installation
### Downloading the Repository
Download the project files using:

> wget https://github.com/harrisongoeldner/primex/archive/php-bridge-server.zip

The repository can also be downloaded with:

> git clone https://github.com/harrisongoeldner/primex.git

### Setting up Dropbox on Device
This project makes use of Dropbox's API. The program can be run without the API being installed however the upload feature will not work. For more information on Dropbox's API for python go to: https://www.dropbox.com/developers/documentation/python

Install Dropbox's API with:
> pip install dropbox

Note: some systems use `pip3` instead of `pip`

### Configuring Dropbox Online

Go to [Dropbox's Developer Page](https://www.dropbox.com/developers) and click `Create App`

Give `files.content.write` permission under the `permissions` tab.

Make note of the `App key` and `App secret` as the program will need those to connect to dropbox.

### First setup of Dropbox

The first time the program runs, assuming the Dropbox API is installed, you will be guided through the connection process.

### Running the Program

To run the program, simply run `main.py`
