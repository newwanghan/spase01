import pymysql
import logging


def get_cursor(db_name):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', charset='utf8',
                           database=str(db_name))
    myCursor = conn.cursor()
    return myCursor


def creat_db(db_name):
    """
    创建数据库
    :param db_name: 数据库名称
    :return: void
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', charset='utf8')
    myCursor = conn.cursor()
    myCursor.execute("CREATE DATABASE {} character set 'utf8'".format(str(db_name)))
    myCursor.close()
    conn.close()


def creat_tables(db_name, table_name):
    """
    创建表
    :param db_name: 数据库名称
    :param table_name: 表名称
    :return: void
    """
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database=str(db_name),
        charset='utf8'
    )
    myCursor = conn.cursor()
    sql = "CREATE TABLE {} (" \
          "id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
          "name VARCHAR(255) UNIQUE, " \
          "age TINYINT DEFAULT NULL, " \
          "gender boolean DEFAULT FALSE, " \
          "testText TEXT, " \
          "img mediumblob DEFAULT NULL)".format(str(table_name))
    myCursor.execute(sql)
    myCursor.close()
    conn.close()


def get_all_tables(db_name):
    """
    获取所有的表名称
    :param db_name: 数据库名称
    :return:一个包含所有表名称的列表
    """
    tableList = []
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()
    myCursor.execute("show tables")
    data = myCursor.fetchall()
    for tableName in data:
        tableList.append(tableName[0])
    myCursor.close()
    conn.close()
    return tableList


def insert_into_table(db_name, table_name, data_dic):
    """
    往数据库里插入一条数据
    :param db_name: 数据库名称
    :param table_name: 表名称
    :param data_dic: 一个字典，键是表的字段，值是要插入的值
    :return: 返回值是最新插入数据的ID
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()

    keys = ', '.join(data_dic.keys())
    values = ', '.join(['%s'] * len(data_dic))
    sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table_name, keys=keys, values=values)
    print(sql)
    try:
        if myCursor.execute(sql, tuple(data_dic.values())):
            logging.info('插入数据成功')
            conn.commit()
            lastID = myCursor.lastrowid
            logging.info(lastID)
            return lastID
    except Exception as e:
        logging.error(e)
        logging.info('插入数据失败')
        conn.rollback()
    finally:
        myCursor.close()
        conn.close()


def update_into_table(db_name, table_name, data_dic):
    """
    如果数据库里面有这条数据，就对这条数据进行修改操作，如果没有，就增加一条数据，进行修改操作时，ID不变
    :param db_name: 数据库名称
    :param table_name: 表名称
    :param data_dic: 一个字典，键是表的字段，值是要插入的值
    :return:  返回值是最新插入数据的ID
    """

    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()
    keys = ', '.join(data_dic.keys())
    values = ', '.join(['%s'] * len(data_dic))
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table_name, keys=keys,
                                                                                         values=values)
    update = ','.join([" {key} = %s".format(key=key) for key in data_dic])
    sql += update
    try:
        if myCursor.execute(sql, tuple(data_dic.values()) * 2):
            logging.info('插入数据成功')
            conn.commit()
            lastID = myCursor.lastrowid
            logging.info(lastID)
            return lastID
    except Exception as e:
        logging.error(e)
        logging.info('插入数据失败')
        conn.rollback()
    finally:
        myCursor.close()
        conn.close()


def replace_into_table(db_name, table_name, data_dic):
    """
    如果数据库里面有这条数据，先删除原来的数据在进行增加，如果没有，就增加一条数据，ID改变。
    :param db_name: 数据库名称
    :param table_name: 表名称
    :param data_dic: 一个字典，键是表的字段，值是要插入的值
    :return: 返回值是最新插入数据的ID
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()

    keys = ', '.join(data_dic.keys())
    values = ', '.join(['%s'] * len(data_dic))
    sql = 'REPLACE INTO {table} ({keys}) VALUES ({values})'.format(table=table_name, keys=keys, values=values)
    try:
        if myCursor.execute(sql, tuple(data_dic.values())):
            logging.info('插入数据成功')
            conn.commit()
            lastID = myCursor.lastrowid
            logging.info(lastID)
            return lastID
    except Exception as e:
        logging.error(e)
        logging.info('插入数据失败')
        conn.rollback()
    finally:
        myCursor.close()
        conn.close()


def del_data(db_name, table_name, condition):
    """
    删除数据
    :param db_name: 数据库名称
    :param table_name: 表名称
    :param condition: 删除的条件
    :return: void
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()
    sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table_name, condition=condition)
    try:
        if myCursor.execute(sql):
            logging.info('删除数据成功')
            conn.commit()
    except Exception as e:
        logging.error(e)
        logging.info('删除数据失败')
        conn.rollback()
    finally:
        myCursor.close()
        conn.close()


def select_data_all(db_name, table_name):
    """
    查询所有的数据
    :param db_name: 数据库名称
    :param table_name: 表名称
    :return: 返回值是一个包含所有数据的元组
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()
    sql = 'SELECT * FROM {table}'.format(table=table_name)
    if myCursor.execute(sql):
        allData = myCursor.fetchall()
        return allData
    else:
        return None


def select_data_one(db_name, table_name):
    """
    查询第一条数据
    :param db_name: 数据库名称
    :param table_name: 表名称
    :return: 包含一条数据的元组
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()
    sql = 'SELECT * FROM {table}'.format(table=table_name)
    if myCursor.execute(sql):
        oneData = myCursor.fetchone()
        return oneData
    else:
        return None


def select_data_many(db_name, table_name, size):
    """
    查询多条数据
    :param db_name: 数据库名称
    :param table_name: 表名称
    :param size: 想要查询的数据 int类型
    :return: 包含多条数据的元组
    """
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database=str(db_name),
                           charset='utf8')
    myCursor = conn.cursor()
    sql = 'SELECT * FROM {table}'.format(table=table_name)
    if myCursor.execute(sql):
        manyData = myCursor.fetchmany(size)
        return manyData
    else:
        return None
