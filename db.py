import pymysql
from datetime import datetime
import random


def connect():
    return pymysql.connect(host='108.61.190.204', user='service',
                           password='123qweQWE', database='shema', charset='utf8', port=3306)



def get_all_projects():
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = f"select distinct project from keywords"
    cursor.execute(sql)
    res = cursor.fetchall()
    c.close()
    return res


def get_all_countries():
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = f"select distinct country from result_scan"
    cursor.execute(sql)
    res = cursor.fetchall()
    c.close()
    return res


def get_geo():
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT DISTINCT country FROM tasks'
    cursor.execute(sql)
    res = cursor.fetchall()
    c.close()
    return res


def get_projects_by_geo(country):
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT DISTINCT project FROM tasks WHERE country = %s'
    cursor.execute(sql, (country,))
    res = cursor.fetchall()
    c.close()
    return res




def add_country(name):
    c = connect()
    cursor = c.cursor()
    sql = f"INSERT INTO countries (name) VALUES (%s);"
    cursor.execute(sql, (name,))
    c.commit()
    c.close()


def get_id_country(name):
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT id FROM countries where name = %s'
    cursor.execute(sql, (name,))
    res = cursor.fetchone()
    c.close()
    return res

def add_proxy(ip,port,real_ip,login,password,country):
    c = connect()
    cursor = c.cursor()
    sql = f"INSERT INTO proxys (ip,port,real_ip,login,password,country,count_used) VALUES (%s,%s,%s,%s,%s,%s,%s);"
    cursor.execute(sql, (ip,port,real_ip,login,password,country,0))
    c.commit()
    c.close()

def check_proxy(country):
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = f"select * from proxys where country = '{country}'"
    cursor.execute(sql)
    res = cursor.fetchone()
    return res

def add_count_proxy(country):
    c = connect()
    cursor = c.cursor(pymysql.cursors.DictCursor)
    sql = f"select * from proxys where country = '{country}'"
    cursor.execute(sql)
    res = cursor.fetchone()
    count = res['count_used']+1
    sql = f"UPDATE proxys SET count_used = {count} where country = '{country}'"
    cursor.execute(sql)
    c.commit()
    c.close()

def delete_proxy(proxy):
    c = connect()
    cursor = c.cursor()
    sql = f"DELETE FROM proxys where proxy = '{proxy}'"
    cursor.execute(sql)
    c.commit()
    c.close()