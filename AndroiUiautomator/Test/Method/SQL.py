#!/user/bin/python
# -*- coding:UTF-8 -*-
import pymysql
import datetime
import json

class ConnectMYSQL:
    def __init__(self):
        self.db = pymysql.connect("114.55.254.134", "sisi.jiang@ecomo.io", "mgLCKe82TIcp77B", "ecomo")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT VERSION()")

    def get_history(self,deviceid,startime = (datetime.datetime.now()-datetime.timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S") ,
        endtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ):
        sql = "select * from ym_water_data where device_id=%s and data_time>'%s' and data_time<'%s'" %(deviceid,startime,endtime)
        print(sql)
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            print(len(results))
            for result in results:
                score = result[1]
                toc = result[2]
                cod = result[3]
                tds = result[4]
                return result
        except:
            return("GET history error!")
        self.db.close()


    def get_event_time(self,deviceid,event_type):
        sql = "select * from ym_device_event where device_id=%s and event_type='%s' order by update_time desc" %(deviceid,event_type)
        print(sql)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except:
            return("GET event_time error!")
        self.db.close()

    def get_favorite_temp(self,deviceid):
        sql = "select favorite from ym_device_info where device_id=%s" %deviceid
        print(sql)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            re = json.loads(result[0])
            temp = re['data'][re['current']]['temperature']
            return temp
        except:
            return ("GET temperature error!")
        self.db.close()
if __name__ == "__main__":
    #s = ConnectMYSQL().get_history(deviceid=73,startime='2020-04-20 15:10:47',endtime='2020-04-28 15:10:47')
    #q =  ConnectMYSQL().get_event_time(deviceid=57,event_type='00')
    t = ConnectMYSQL().get_favorite_temp(25)
    print(t)



