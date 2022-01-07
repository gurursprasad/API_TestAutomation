import time
import pytest
import logging
import json
import requests

from utilities.BaseClass import BaseClass
from utilities.configs import *
from utilities.utils import *


class Test_Time_Series_Intraday_API(BaseClass):
    @pytest.mark.TestThrottleLimit
    def test_throttle_5_per_min(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 5 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS, 1)
        log.info("Completed running 5 requests")
        log.info("Waiting for 60 sec...")

    @pytest.mark.TestThrottleLimit
    def test_throttle_6_for_2_min(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 5 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS, 1)
        log.info("Completed running 5 requests")
        log.info("Waiting for 60 sec...")
        t = request_time(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS)
        log.info("6th request executed in the next minute with status code '%d'" % get_status_code(self.base_url,
                                                                                                   TIME_SERIES_INTRADAY_USER1_PARAMS))
        log.info("6 requests executed in 2 minutes")
        log.info("Waiting for 60 sec...")
        wait_for_60sec()

    @pytest.mark.TestThrottleLimitxx
    def test_throttle_6_per_min(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 5 requests")
        run_5_requests_every_minute_without_wait(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS, 1)
        log.info("Completed running 5 requests")
        t = request_time(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS)
        log.info("Next Request took %.5f ms with status code '%d'" % (
            t, get_status_code(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS)))
        assert get_status_code(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS) == 429
        log.info("Waiting for 60 sec...")
        wait_for_60sec()

    @pytest.mark.TestThrottleLimit
    def test_throttle_500_per_day(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 500 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS, 100)
        log.info("Completed running 500 requests")
        log.info("Waiting for 60 sec...")

    @pytest.mark.TestThrottleLimit
    def test_throttle_501_per_day(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 500 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS, 100)
        log.info("Completed running 500 requests")
        log.info("Running the 501'th request")
        t = request_time(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS)
        log.info("Next Request took %.5f ms with status code '%d'" % (
            t, get_status_code(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS)))
        assert get_status_code(self.base_url, TIME_SERIES_INTRADAY_USER1_PARAMS) == 429
        log.info("Execution completed")
        log.info("Waiting for 60 sec...")
        wait_for_60sec

    @pytest.mark.TestThrottleLimit
    def test_throttle_500_per_day_for_different_user(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 500 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_USER2_PARAMS, 100)
        log.info("Completed running 500 requests")
        log.info("Waiting for 60 sec...")

    @pytest.mark.TestOptionalParams
    def test_optional_params1(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 5 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_OPTIONAL_PARAMS1, 1)
        log.info("Waiting for 60 sec...")
        log.info("Completed running 5 requests")

    @pytest.mark.TestOptionalParams
    def test_optional_params2(self, setup_base_url):
        log = self.getLogger()
        log.info("Started running 5 requests")
        run_5_requests_every_minute(self.base_url, TIME_SERIES_INTRADAY_OPTIONAL_PARAMS2, 1)
        log.info("Waiting for 60 sec...")
        log.info("Completed running 5 requests")