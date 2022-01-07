import time
import requests
from urllib.request import urlopen
from utilities.configs import *

"""
    This method is to return the execution time of a request hitting the endpoint and getting the response from the endpoint
    It takes (url) and (params) as arguments

"""


def request_time(url, params):
    start_time = time.time()
    r = requests.get(url=url, params=params, )
    end_time = time.time()
    return end_time - start_time


"""
    This method is to return the status code
    IT takes (url) and (params) as arguments

"""


def get_status_code(url, params):
    r = requests.get(url=url, params=params, )
    return r.status_code


"""
    This method is to run "5" requests every minute.
    IT takes (url), (params) and (Total number of requests/5) as arguments

"""


def run_5_requests_every_minute(url, params, total_no_of_requests_by_5):
    i = 1
    while i <= total_no_of_requests_by_5:
        request_count = 5
        for i in range(request_count):
            t = request_time(url, params)
            print("Request #%d took %.5f ms with status code '%d'" % (i + 1, t, get_status_code(url, params)))
        print("--- Throttling Limit Reached ---")
        print("Waiting for 60 sec...")
        wait_for_60sec()
        i = i + 1
    print("5 requests Executed")


"""
    This method is to run "5" requests every minute.
    IT takes (url), (params) and (Total number of requests/5) as arguments

"""


def run_5_requests_every_minute_without_wait(url, params, total_no_of_requests_by_5):
    i = 1
    while i <= total_no_of_requests_by_5:
        request_count = 5
        for i in range(request_count):
            t = request_time(url, params)
            print("Request #%d took %.5f ms with status code '%d'" % (i + 1, t, get_status_code(url, params)))
        print("--- Throttling Limit Reached ---")
        i = i + 1
    print("5 requests Executed")


"""
    This method is to return the status code
    IT takes (url) and (params) as arguments

"""


def wait_for_60sec():
    print("Waiting for 60 sec...")
    time.sleep(60)
