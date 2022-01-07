# API_TestAutomation using Python-Pytest

## Description: 
* Pytest is a framework that helps us to write and run tests in Python.
* The requests module helps us to send http requests using python

## Getting Started:
* Run `pip install pytest` to download and install pytest
* Run `pip install requests` to download and install requests

To ensure all dependencies are resolved in a CI environment, in one go, add them to a `requirements.txt` file.
* Then run the following command : `pip install -r requirements.txt`


## Running Tests:
* The tests are located in the `API_TestAutomation\tests` directory. Go to this directory
* Use `py.test --endpoint=<endpoint IP> --html=reports.html` to run all tests
* Use `py.test --endpoint=<endpoint IP> --html=reports.html -m <markname> -v -s` to run specific tests.
* The log file will get created inside `API_TestAutomation\tests` directory as `logfile.log`
* After the test run completes the html report gets generated inside `API_TestAutomation\tests` directory as `reports.html`


## Custom Marks used:
* `@pytest.mark.TestThrottleLimit`. This mark is to run throttling limt related scenarios. Use `py.test --endpoint=<endpoint IP> --html=reports.html -m TestThrottleLimit -v -s` to run these test scripts.
* `@pytest.mark.TestOptionalParams`. This mark is to run optional parameters related scenarios. Use `py.test --endpoint=<endpoint IP> --html=reports.html -m TestOptionalParams -v -s` to run these test scripts.

## Configs Used:
* All the configs are given here `API_TestAutomation\utilities\configs.py`
