#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: handling of errors

# As required per statbureau's ToS, the data comes from:
# - https://www.statbureau.org/

import http.client, re
conn = http.client.HTTPSConnection("www.statbureau.org")

p = re.compile("[0-9.]+")

country = "eurozone"
value = 100
start = "2012/12/01"
end = "2015/12/01"

conn.request("GET", "/calculate-inflation-price-jsonp?country=" + country + "&start=" + start + "&end=" + end + "&amount=" + str(value))
res = conn.getresponse()
print(p.search(res.read().decode("utf-8")).group())
conn.close()
