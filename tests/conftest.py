import pytest
from selenium import webdriver

from utilities.configs import *


def pytest_addoption(parser):
    parser.addoption(
        "--endpoint", action="store", default="alphavantage"
    )


@pytest.fixture(scope="class")
def setup_base_url(request):
    global base_url
    endpoint = request.config.getoption("endpoint")
    if endpoint == "alphavantage":
        base_url = ENDPOINTS["alphavantage"]
    elif endpoint == "localhost":
        base_url = ENDPOINTS["localhost"]

    request.cls.base_url = base_url
