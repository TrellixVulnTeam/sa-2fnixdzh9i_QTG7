# Copyright (c) 2018-present, Taatu Ltd.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from sa_db import *
access_obj = sa_db_access()
import pymysql.cursors


db_usr = access_obj.username(); db_pwd = access_obj.password(); db_name = access_obj.db_name(); db_srv = access_obj.db_server()

def get_portf_perf(uid):

    portf_perf_box = ''


    try:
        connection = pymysql.connect(host=db_srv,user=db_usr,password=db_pwd, db=db_name,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        cr = connection.cursor(pymysql.cursors.SSCursor)
        sql = "SELECT chart_data.symbol, chart_data.date, chart_data.price_close, instruments.fullname, instruments.unit FROM chart_data "+\
        "JOIN instruments ON chart_data.symbol = instruments.symbol "+\
        "WHERE chart_data.uid=" + str(uid) + " ORDER BY chart_data.date"
        print(sql)
        cr.execute(sql)
        rs = cr.fetchall()
        data = ""
        for row in rs:
            symbol = row[0]
            chart_date = row[1]
            price_close = row[2]
            fullname = row[3]
            portf_unit = row[4]

            year = chart_date.strftime("%Y")
            month = chart_date.strftime("%m")
            day = chart_date.strftime("%d")
            if data =="":
                data = data + "[new Date("+str(year)+", "+str(int(month)-1 )+", "+str(day)+"),"+str(price_close)+"]"
            else:
                data = data + ",[new Date("+str(year)+", "+str( int(month)-1 )+", "+str(day)+"),"+str(price_close)+"]"


        box_title = "Portfolio 1-Year Performance"
        hAxis = "Date"; vAxis = "Price (" + portf_unit + ")"
        profit_1Y = price_close
        portf_perf_font_size = 10

        portf_perf_box = '' +\
        '        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">'+\
        '            <div class="box-part sa-portf-perf-portf-chart">'+\
        '                   <div><h5>'+ box_title +'</h5></div>'+\
        '                   <script>'+\
        '                       google.charts.load("current", {"packages":["corechart"]});'+\
        '                       google.charts.setOnLoadCallback(drawChart);'+\
        '                       function drawChart() {'+\
        '                          var data = new google.visualization.DataTable();'+\
        '                          data.addColumn("date", "'+ hAxis +'");'+\
        '                          data.addColumn("number", "'+ vAxis +'");'+\
        '                          data.addRows(['+data+']);'+\
        '                          var options = {'+\
        '                            legend: "none",'+\
        '                            vAxis: {minValue: 0, textStyle: {fontSize:'+ str(portf_perf_font_size) +'}, gridlines: { color: "transparent" } },'+\
        '                            hAxis: {textStyle: {fontSize:'+ str(portf_perf_font_size) +'} }, '+\
        '                            series:{0: {areaOpacity: 0.1, color: "black", lineWidth: 1} },'+\
        '                            chartArea:{width:"80%",height:"80%"}'+\
        '                          };'+\
        '                          var chart = new google.visualization.AreaChart(document.getElementById("portf_perf_chart"));'+\
        '                          chart.draw(data, options);'+\
        '                       }'+\
        '                   </script>'+\
        '               <div id="portf_perf_chart" class="sa-chart-hw-100"></div>'+\
        '            </div>'+\
        '        </div>'


        cr.close()
        connection.close()


    except Exception as e: print(e)

    return portf_perf_box
