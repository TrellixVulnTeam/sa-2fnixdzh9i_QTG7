# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()

def get_user_creation_form(burl):

    box_content = ''

    try:

        box_content = '<div class="box-top">' +\
        '   <div>'+\
        '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
        '            <div class="box-part disable-overflow">'+\
        '     <form method="POST" action="'+ burl +'n/?uid=xxx">'+\
        '         <div>'+\
        '            <div>'+\
        '                <h3 style="text-align: center;">Join SmartAlpha today.</h3>'+\
        '                <hr>'+\
        '            </div>'+\
        '        </div>'+\
        '        <div>'+\
        '            <div>'+\
        '                <div class="form-group">'+\
        '                    <div class="input-group mb-2 mr-sm-2 mb-sm-0">'+\
        '                        <div class="input-group-addon" style="width: 2.6rem"><i class="fa fa-user"></i></div>'+\
        '                        <input type="text" name="name" class="form-control" id="name" placeholder="Your name" required autofocus>'+\
        '                    </div>'+\
        '                </div>'+\
        '            </div>'+\
        '        </div>'+\
        '        <div>'+\
        '            <div>'+\
        '                <div class="form-group">'+\
        '                    <div class="input-group mb-2 mr-sm-2 mb-sm-0">'+\
        '                        <div class="input-group-addon" style="width: 2.6rem"><i class="fa fa-at"></i></div>'+\
        '                        <input type="text" name="email" class="form-control" id="email" placeholder="Your email: you@example.com" required autofocus>'+\
        '                    </div>'+\
        '                </div>'+\
        '            </div>'+\
        '        </div>'+\
        '        <div>'+\
        '            <div>'+\
        '                <div class="form-group has-danger">'+\
        '                    <div class="input-group mb-2 mr-sm-2 mb-sm-0">'+\
        '                        <div class="input-group-addon" style="width: 2.6rem"><i class="fa fa-key"></i></div>'+\
        '                        <input type="password" name="password" class="form-control" id="password" placeholder="Password" required>'+\
        '                    </div>'+\
        '                </div>'+\
        '            </div>'+\
        '        </div>'+\
        '        <div>'+\
        '            <div>'+\
        '                <button type="submit" class="btn btn-success btn-lg btn-block form-signin-btn"><i class="fa fa-user-plus"></i> Sign up</button>'+\
        '            </div>'+\
        '        </div>'+\
        '    </form>'+\
        '            </div>'+\
        '        </div>'+\
        '   </div>'+\
        '</div>'


        box_content = box_content + '<div class="box">' +\
        '   <div class="row">'+\
        '        <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">'+\
        '            <div class="box-part">'+\
        '            </div>'+\
        '        </div>'+\
        '   </div>'+\
        '</div>'

    except Exception as e: print(e)

    return box_content
