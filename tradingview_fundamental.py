# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors

db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_tradingview_fundamental(suid):
    r = ''
    url = 'http://smartalphatrade.com/s/'
    try:
        symbol = ''
        referral_id = 'smartalpha'
        label_not_available = 'Fundamental data is not available for this instrument'

        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT tradingview FROM symbol_list WHERE uid ='"+ str(suid) +"'"
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs: symbol = row[0]

        if symbol != '':
            r = '' +\
            '<div class="tradingview-widget-container">'+\
            '  <div class="tradingview-widget-container__widget"></div>'+\
            '  <div class="tradingview-widget-copyright"><a href="https://www.tradingview.com/symbols/NASDAQ-AAPL/" rel="noopener" target="_blank"><span class="blue-text">Fundamental Data</span></a> by TradingView</div>'+\
            '  <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-financials.js" async>'+\
            '  {'+\
            '  "symbol": "'+ symbol +'",'+\
            '  "colorTheme": "light",'+\
            '  "isTransparent": true,'+\
            '  "largeChartUrl": "'+ url +'",'+\
            '  "displayMode": "compact",'+\
            '  "width": "100%",'+\
            '  "height": "510",'+\
            '  "locale": "en"'+\
            '}'+\
            '  </script>'+\
            '</div>'
        else:
            r = label_not_available

    except Exception as e: print(e)
    return r
