#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: handling of errors
# TODO: print usage etc

# As required per statbureau's ToS, the data comes from:
# - https://www.statbureau.org/

currencies = {  "USD": "united-states",
                "UAH": "ukraine",
                "EUR": "eurozone",
                "CHF": "switzerland",
                "PLN": "poland" }

import http.client, re, sys
conn = http.client.HTTPSConnection("www.statbureau.org")

p = re.compile("[0-9.]+")

conn.request("GET", "/calculate-inflation-price-jsonp?country=" + currencies[sys.argv[2]]
    + "&start=" + sys.argv[3]
    + "&end=" + sys.argv[4]
    + "&amount=" + sys.argv[1])
res = conn.getresponse()
print(p.search(res.read().decode("utf-8")).group())
conn.close()
