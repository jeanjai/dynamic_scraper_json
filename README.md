# Dynamic Selenium Web Scraper from Json input

## Table of contents
* [Desctription](#description)
* [Features](#features)
* [Requirements](#requirements)
* [How to run a scrape](#how-to-run-a-scrape)
* [Data types](#data-types)

## Description:
This dynamic scraper uses python and selenium to extract data from websites based on selectors and actions defined in a json file ```config.json```.

## Features:
* Wide list of actions to gather data
* Option for multiple start urls
* Run either headless or display visually
* Can gather data rendered with javascript
* Ability to create nested actions
* Export results in either a csv or an object

## Requirements:
* [Python](https://www.python.org/downloads/)
* [Selenium](https://www.seleniumhq.org/download/)
* Requests ```pip install requests```
* Chrome version 84 (if using pre-installed chromedriver)

## How to run a scrape:

### **Step 1:**

Install the required packages.
* [Python](https://www.python.org/downloads/)
* [Selenium](https://www.seleniumhq.org/download/)
* Requests ```pip install requests```

To make sure the packages are downloaded properly, do the following:
* In terminal enter ```python```. If no error are shown, python is successfully downloaded
* In terminal enter ```python``` and after enter ```import selenium```. If no error are shown, selenium is successfully downloaded
* In terminal enter ```python``` and after enter ```import requests```. If no error are shown, requests is successfully downloaded

### **Step 2:**

In the ```config.json``` file, replace the file with your desired actions and settings for your scrape. You can also see some examples in the json_exceptions folder.

### **Step 3:**

Run the ```run.py``` file in terminal ```python run.py```

## Data types:

Every data type does specific actions based on what is defined in the ```commands.py``` file. Different actions can require different inputs.

### Here's a list of current actions:
* **```enterText```** - Inputs a ```value``` in a given ```selector```
* **```selectorText```** - Gets the text ```value``` of a given ```selector```. It can also grab multiple text values if ```multiple``` is set to ```true```
* **```selectorLink```** - Gets the href of a ```selector```. It can also grab multiple taxt value if ```multiple``` is set to true
* **```getAttribute```** - Gets an ```attribute```'s text value of a given ```selector```. It can also grab multiple attribute values if ```multiple``` is set to ```true```
