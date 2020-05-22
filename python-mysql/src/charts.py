# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 16:05:13 2015

@author: metivier
"""
import urllib2
from bs4 import BeautifulSoup
from matplotlib.pylab import *

import MySQLdb

class OpenDB:
    
    def __init__(self,dbase):
        self.base=dbase
        self.conn=MySQLdb.connect(host="localhost",user="root",passwd="iznogod01",db=self.base,charset='utf8')
        #self.conn=MySQLdb.connect(host="localhost",user="root",passwd="iznogod01",db=self.base)

    def execQuery(self,req,param=()):
        cursor=self.conn.cursor()
        try:
            cursor.execute(req,param)
        except Exception as err:
            # send back the message
            msg="Incorrect SQL Query    : \n%s\nError detected:"%(req)    
            return msg+str(err)
        res=[]
        if "SELECT" in req.upper():
            res= cursor.fetchall()
        elif "DESCRIBE" in req.upper():
            res= cursor.fetchall()
        else:
            self.conn.commit()
        cursor.close()
        return res

    def close(self):
        self.conn.close()


def retrieve_charts():
    
    o=OpenDB("Charts")
    
    for y in arange(1):
        y+=118
        year=1900+y
        if y < 100:
            yy=y
        elif y>=100 and y <110:
            yy="0%s" % (y-100)
        else:
            yy=y-100
        print yy
        
        #for i in arange(52)+1:
        for i in [46,47,48,49,50,51,52]:
            week=i
            if i<10:
                st='%s0%s' % (yy,i)
            else:
                st='%s%s' % (yy,i)
            
            print st
            turl="http://www.chartsinfrance.net/charts/%s/singles.php" %st
            page=urllib2.urlopen(turl)
            soup = BeautifulSoup(page)
            
            
            a=soup.findAll("div","c1_td1")
            
            for div in a:
                record=[]
                rank=div.findAll("div","c1_td2")
                for r in rank:
                    record.append(r.contents[0])
                    print "rang :", r.contents[0]
                rank=div.findAll("div","c1_td5")
                for r in rank:
                    aa=r.findAll("a")
                    if len(aa)==2:
                        record.append(aa[0].contents[0])
                        record.append(aa[1].contents[0])
                        print "artiste:", aa[0].contents[0]
                        print "titre:", aa[1].contents[0]
                    elif len(aa)==1:
                        try:
                            bb=r.findAll("font")
                            record.append(bb[0].contents[0])
                            record.append(aa[0].contents[0])
                            print "artiste:", bb[0].contents[0]
                            print "titre:", aa[0].contents[0]
                        except:
                            print 'merdeuu'
                    try:
                        sql="insert into SingleFrance values (%s,%s,%s,%s,%s)"
                        res=o.execQuery(sql,(year,week,record[0],record[1].encode('utf-8'),record[2].encode('utf-8')))
                        print res
                    except:
                        print 'merdeuuu'
                        
                print "==================================================="
        
    o.close()
        #print table
        
def retrieve_charts_this_year():
    
    o=OpenDB("Charts")
    
    year=2018    
    yy='17'        
    for i in arange(47)+1:
        week=i
        if i<10:
            st='%s0%s' % (yy,i)
        else:
            st='%s%s' % (yy,i)
        
        turl="http://www.chartsinfrance.net/charts/%s/singles.php" %st
        page=urllib2.urlopen(turl)
        soup = BeautifulSoup(page)
        
        
        a=soup.findAll("div","c1_td1")
        
        for div in a:
            record=[]
            rank=div.findAll("div","c1_td2")
            for r in rank:
                record.append(r.contents[0])
                print "rang :", r.contents[0]
            rank=div.findAll("div","c1_td5")
            for r in rank:
                aa=r.findAll("a")
                if len(aa)==2:
                    record.append(aa[0].contents[0])
                    record.append(aa[1].contents[0])
                    print "artiste:", aa[0].contents[0]
                    print "titre:", aa[1].contents[0]
                elif len(aa)==1:
                    try:
                        bb=r.findAll("font")
                        record.append(bb[0].contents[0])
                        record.append(aa[0].contents[0])
                        print "artiste:", bb[0].contents[0]
                        print "titre:", aa[0].contents[0]
                    except:
                        pass
                    

                sql="insert into SingleFrance values (%s,%s,%s,%s,%s)"
                res=o.execQuery(sql,(year,week,record[0],record[1].encode('utf-8'),record[2].encode('utf-8')))
                print res
                print res
            print "==================================================="
        
    o.close()
        #print table

def get_artists(page):
    soup = BeautifulSoup(page)
            
            
    a=soup.findAll("div","c1_td1")
    
    for div in a:
        record=[]
        rank=div.findAll("div","c1_td2")
        for r in rank:
            record.append(r.contents[0])
            print "rang :", r.contents[0]
        rank=div.findAll("div","c1_td5")
        for r in rank:
            aa=r.findAll("a")
            if len(aa)==2:
                record.append(aa[0].contents[0])
                record.append(aa[1].contents[0])
                #print "artiste:", aa[0].contents[0]
                #print "titre:", aa[1].contents[0]
            else:
                print "???", aa
        
                #sql="insert into SingleFrance values (%s,%s,%s,%s,%s)"
                #res=o.execQuery(sql,(year,week,record[0],record[1],record[2]))
                #print res
        print "==================================================="
       

def pdf_10():
    
    o=OpenDB("Charts")

    sql="""select avg(nw), count(nw) from (select artist, count(*) as nw from SingleFrance group by artist,song) as c1 group by artist having count(*) > 10 order by avg(nw) ASC;
    """
    
    res=o.execQuery(sql)
    out=transpose(array(res))
    a=out[0]
    sa=out[1]
    print a
    
    figure()
    hist(a.astype(int),20,normed=True)
    bins=arange(1,20,1)
    y=normpdf(bins,mean(a.astype(float)),std(a.astype(float)))
    plot(bins,y,'r--',label='r',linewidth=3)

    
    show()
    o.close()
    

#pdf_10()
#turl="http://www.chartsinfrance.net/charts/1450/singles.php" 
#page=urllib2.urlopen(turl)
#get_artists(page)        

#retrieve_charts()
retrieve_charts_this_year()
