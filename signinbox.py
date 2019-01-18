# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_func import *
from signin_main import *

def get_signin_box(burl):

    box_content = ''

    try:

        box_content = '<div class="box-sign"><div class="row">' +\
        '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
        '            <div class="sign-part">'+\
        '               <div class="row sign-row">'+\
        '                <div class="col-lg-6 col-md-6 col-sm-23 col-xs-12 sa-signin-box">'+\
        '                   <div>&nbsp;</div>'+\
        '                   <h1 style="text-align: left;">A.I. powered Trading Insights</h1>   '+\
        '                   <div>Your personal trading assistant. Access to more than 1,000 financial instruments, stocks, forex, commodities & cryptos. Get daily signals powered by Artificial intelligence.</div>'+\
        '                </div>'+\
        '                <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12" style="padding: 50px;">'+\
        get_login_form(burl) +\
        '                </div>'+\
        '               </div>'+\
        '            </div>'+\
        '        </div>'+\
        '</div></div>'

        cr.close()
        connection.close()

    except Exception as e: print(e)

    return box_content
