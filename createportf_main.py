
from flask import Flask, make_response, request, redirect
from app_page import *
from app_head import *
from app_ogp import *
from app_metatags import *
from app_title import *
from app_body import *
from bootstrap import *
from app_loading import *
from app_stylesheet import *
from app_navbar import *
from font_awesome import *
from app_cookie import *
from sa_func import *
from googleanalytics import *
from list_instr_n_portf import *
from portf_gen_user_example import *
from portf_save import *
import datetime
import time
from datetime import timedelta

from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors


db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()


def get_selectportf_box(burl,step,mode,x):
    box_content = ''
    min_sel = '5'
    progress_value = '0'

    if step == '1':
        l_desc_part_1 = "Select from list."
        progress_value = '20'
    if step == '2':
        l_desc_part_1 = str(step) +" of "+ str(min_sel)
        progress_value = '40'
    if step == '3':
        l_desc_part_1 = str(step) +" of "+ str(min_sel)
        progress_value = '60'
    if step == '4':
        l_desc_part_1 = str(step) +" of "+ str(min_sel)
        progress_value = '80'
    if step == '5':
        l_desc_part_1 = str(step) +" of "+ str(min_sel)
        progress_value = '95'
    if step == '6':
        l_desc_part_1 = "Save strategy"
        progress_value = '100'

    l_back_button = 'back'
    l_skip_process_button = 'done'

    button_back = '<span style="float:left;"><button type="button" style="font-size: medium;" class="btn btn-lg btn-secondary" onClick="javascript:history.back();"><i class="fas fa-caret-left"></i>&nbsp;'+ l_back_button +'</button></span>'
    if step != '1' and step != '2' and step != '6':
        button_process_skip = '<span style="float:right;"><a href="'+ burl + 'p/?ins=3' +'" style="font-size: medium;" class="btn btn-lg btn-secondary">'+ l_skip_process_button +'&nbsp;<i class="fas fa-forward"></i></a></span>'
    else:
        button_process_skip = ''

    portf_selection = '<h6>'
    for i in range(5):
        select_instr = get_portf_select(i+1)
        if not select_instr == '':
            portf_selection = portf_selection + '<span class="badge badge-info"><i class="fas fa-chart-pie">&nbsp;</i>'+ select_instr +'</span>&nbsp;&nbsp;'
    portf_selection = portf_selection + '</h6>'

    if int(step) > 1 and int(step) < 6:
        portf_selection = 'your strategy selection: ' + portf_selection
    else:
        portf_selection = ''

    box_content = '<div class="box-top">' +\
    '   <div class="row">'+\
    '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
    '            <div class="box-part sa-center-content rounded">'+\
    '                   <div class="alert" role="alert">' +\
    '                       <h5><i class="fas fa-list-ol"></i>&nbsp;'+ l_desc_part_1 +'</h5>'+ button_back + '&nbsp;&nbsp;&nbsp;&nbsp;' + button_process_skip +\
    '                          <div>&nbsp;</div> '+\
    '                          <div class="progress">'+\
    '                               <div class="progress-bar progress-bar-striped bg-success" role="progressbar" style="width: '+ str(progress_value) +'%" aria-valuenow="'+ str(progress_value) +'" aria-valuemin="0" aria-valuemax="100"></div>'+\
    '                          </div>'+\
    '                   </div>'+\
    portf_selection +\
    '            </div>'+\
    '        </div>'+\
    '   </div>'+\
    '</div>'
    return box_content

def save_portf_select(appname,burl,step,mode,x,portf,uid):
    next_step = int(step) +1
    if int(step) < 5:
        resp = make_response( redirect(burl+'p/?ins=1&step='+ str(next_step) ) )
        resp.set_cookie('portf_s_'+str(step), str(uid), expires=datetime.datetime.now() + datetime.timedelta(days=1) )
    else:
        resp = make_response( redirect(burl+'p/?ins=3' ) )
        resp.set_cookie('portf_s_'+str(step), str(uid), expires=datetime.datetime.now() + datetime.timedelta(days=1) )
    return resp

def get_portf_select(select):
    return_data = ''
    uid = request.cookies.get('portf_s_' + str(select) )
    if not uid is None or uid == '':
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT instruments.fullname FROM instruments JOIN symbol_list ON instruments.symbol = symbol_list.symbol "+\
        "WHERE symbol_list.uid=" + str(uid)
        cr.execute(sql)
        rs = cr.fetchall()
        for row in rs: return_data = row[0]
        cr.close()
    return return_data

def ini_portf_select(r):
    resp = make_response(r)
    conviction = 'neutral'
    for i in range(5):

        if get_random_num(3) == 1: conviction = 'neutral'
        if get_random_num(3) == 2: conviction = 'weak'
        if get_random_num(3) == 3: conviction = 'strong'

        resp.set_cookie('portf_s_' + str(i+1),'0',expires=datetime.datetime.now() + datetime.timedelta(days=1) )
        resp.set_cookie('portf_s_' + str(i+1) + '_type','long/short',expires=datetime.datetime.now() + datetime.timedelta(days=1) )
        resp.set_cookie('portf_s_' + str(i+1) + '_conv',conviction,expires=datetime.datetime.now() + datetime.timedelta(days=1))
    return resp

def gen_selectportf_page(appname,burl,step,mode,x,portf):
    return_data = ''
    return_data = get_head( get_loading_head() + get_googleanalytics() + get_title( appname ) + get_metatags(burl) + set_ogp(burl,1,'','') + get_bootstrap( get_sa_theme(),burl ) + get_font_awesome() + get_stylesheet(burl) )
    return_data = return_data + get_body( get_loading_body(), navbar(burl,0) + get_selectportf_box(burl,step,mode,'') + get_box_list_instr_n_portf(burl,'portf_select','instr',step,1000,'') )
    return_data = set_page(return_data)
    if step == '1': return_data = ini_portf_select(return_data)
    return return_data

def custom_save_portf_page(appname,burl,mode,x):
    return_data = get_head( get_loading_head() + get_googleanalytics() + get_title( appname ) + get_metatags(burl) + set_ogp(burl,1,'','') + get_bootstrap( get_sa_theme(),burl ) + get_font_awesome() + get_stylesheet(burl) )
    return_data = return_data + get_body( get_loading_body(), navbar(burl,0) + get_selectportf_box(burl,'6',mode,'') + get_box_portf_save(burl) )
    return_data = set_page(return_data)
    return return_data
