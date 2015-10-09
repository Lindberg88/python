'''
Created on Oct 8, 2015

@author: andreaslindberg
'''

from googlefinance import getQuotes
import json

print json.dumps(getQuotes('CSCO'),indent=2)

print json.dumps(getQuotes('AAPL'),indent=2)

print json.dumps(getQuotes('002502'),indent=2)

print 'Klar!'