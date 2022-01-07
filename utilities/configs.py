ENDPOINTS = {
    "alphavantage": "https://www.alphavantage.co/query?",
    "localhost": "http://localhost:3000/"
}
TIME_SERIES_INTRADAY_USER1_PARAMS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "15min",
    "slice": "year1month1",
    "apikey": "1KG2ZTH0DXTTOB47"
}
"""
    To test Throttling Limit of 500 per day we need multiple logins
    In this case it can be "apikey" or any other parameter that we are passing
    Going with the assumption it is "apikey"
    To test 500 per day scenario we'll use "TIME_SERIES_INTRADAY_USER2_PARAMS"
"""
TIME_SERIES_INTRADAY_USER2_PARAMS = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "15min",
    "slice": "year1month1",
    "apikey": "1KG2ZTH0DXTTOB47"
}
TIME_SERIES_INTRADAY_OPTIONAL_PARAMS1 = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "30min",
    "adjusted": "true",
    "outputsize": "compact",
    "datatype": "json",
    "slice": "year1month1",
    "apikey": "1KG2ZTH0DXTTOB47"
}
TIME_SERIES_INTRADAY_OPTIONAL_PARAMS2 = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": "IBM",
    "interval": "60min",
    "adjusted": "false",
    "outputsize": "full",
    "datatype": "json",
    "slice": "year1month1",
    "apikey": "1KG2ZTH0DXTTOB47"
}