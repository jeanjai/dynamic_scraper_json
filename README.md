# Dynamic Selenium Web Scraper from Json input

### Please note that this is still a work in progress

## Table of contents
* [Desctription](#description)
* [Features](#features)
* [Requirements](#requirements)
* [How to run a scrape](#how-to-run-a-scrape)
* [Data types](#data-types)

## Description:
This dynamic scraper uses python and selenium to extract data from websites based on selectors and actions defined in a json file ```config.json```.

## Features:
* Wide list of export data types
* Ability to scrape multiple websites using 1 json file
* Ability to do actions on the page based on inputs in json file

## Requirements:
* [Python](https://www.python.org/downloads/)
* [Selenium](https://www.seleniumhq.org/download/)
* Requests ```pip install requests```
* Chrome version 78 (with current chrome driver)

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

In the ```config.json``` file, enter the actions, and start url for your scrape. You can also use the example_config.json file as a sample.

### **Step 3:**

Run the ```run.py``` file in terminal ```python run.py```

## Config.json file:
```

{
    "example": {
        "url": ["example.com"], #list of urls
        "actions": [
            {
                "type": "enterText",
                "value": "foo",
                "selector": "#search_keyword"
            },
            {
                "type": "enterText",
                "value": "foo",
                "selector": "#search_location"
            },
            {
                "type": "click",
                "selector": "#btn_search",
                "multiple": false
            }
        ]
    },
    "example2": {
      "url": ["exampletwo.com"], #list of urls
        "actions": [ 
            {
                "type": "enterText",
                "value": "bar",
                "selector": "#search_keyword"
            },
            {
                "type": "enterText",
                "value": "foo",
                "selector": "#search_location"
            },
            {
                "type": "click",
                "selector": "#btn_search",
                "multiple": false
            }
        ]
    }
}
```

## Data types:

Every data type does specific actions based on what is defined in the ```commands.py``` file. Different actions can require different variables.

### Here's a list of current actions:
* **```enterText```** - Inputs a ```value``` in a given ```selector```
* **```getValue```** - Gets the text ```value``` of a given ```selector```. It can also grab multiple text values if ```multiple``` is set to ```true```
* **```getAttribute```** - Gets an ```attribute```'s text value of a given ```selector```. It can also grab multiple attribute values if ```multiple``` is set to ```true```
* **```click```** - Clicks a given ```selector```
* **```getLink```** - Gets the href of a ```selector```. It can also grab multiple taxt value if ```multiple``` is set to true
