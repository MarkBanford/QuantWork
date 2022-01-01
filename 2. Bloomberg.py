from xbbg import blp

tickers = ['FR0013534518 GOVT', 'MX0MG0000102 GOVT']
analytics = ['IS_UNIT_TRADED', 'PX_LAST']

results = blp.bdp(tickers=tickers, flds=analytics)

print(results.head(5))
