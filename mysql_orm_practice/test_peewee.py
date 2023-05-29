from datetime import datetime
from peewee import *
from playhouse.migrate import *
from playhouse.pool import PooledMySQLDatabase

HOST = 'localhost'
USERNAME = 'root'
PASSWORD = '123456'
PORT = 3306
DATABASE = 'test'

# Connect to a MySQL database on network.
mysql_db = MySQLDatabase(DATABASE, user=USERNAME, password=PASSWORD,
                         host=HOST, port=PORT)
db_pool = PooledMySQLDatabase(DATABASE, max_connections=32, stale_timeout=500, user=USERNAME, password=PASSWORD,
                            host=HOST, port=PORT)
"""
不使用连接池，连接用完记得close，释放资源
使用mysql数据连接池:
    1.连接用完记得close(假意义的close)，让连接回到池子中，可以复用
    param:
        max_connections: 连接池的最大连接数
        stale_timeout: 连接允许使用的时长 (seconds)
        time_out: 连接池满了后，block的时长，默认当连接池满了，不会block而是直接抛异常；可以设置为0表示无限期的block下去
    
    2.对于单线程应用，连接池只创建一个连接，然后重复使用，直到连接使用超过最长使用时长，则真正close，然后继续只创建一个新的
    3.对于多线程，最多创建max_connections个连接，每个线程拥有自己的连接

"""
# PooledMySQLDatabase()

"""
数据表只创建一次，重复执行无效，如果表中列有增、删、改都需要额外使用schema migration api
"""
class TakaCrawlerRecord(Model):
    app_name = CharField(default='instagram')
    profile_name = CharField()
    crawled_publisher_id = CharField()
    status = CharField()
    total = IntegerField()
    success_num = IntegerField()
    failed_num = IntegerField()
    # ctime = DateField(default=datetime.now)
    ctime = DateTimeField(default=datetime.now)
    description = CharField(default='xxx')

    class Meta:
        # database = mysql_db
        database = db_pool
        table_name = 'taka_crawler_record'


# print(mysql_db.connect())
mysql_db.create_tables([TakaCrawlerRecord])

"""
当把ctime数据类型改完DateTime后，Model中的ctime也得改成Datetime，因为Model只是提供了值的输入，所以老的DateField还是会把datetime.now
截取为Date类型，只是DB中的列改为了DateTime了，所以存到DB中的效果就是时间部分都是00

Model作为ORM提供输入输出，只在初次创建表的时候起决定column类型的作用；
后期DB column 增删改的修改通过Model的字段类型无法实现，只能有Migrator额外修改，然后同步Model(migrator 增加字段后，需要在Model中加回来)

"""
# migrator = MySQLMigrator(mysql_db)
# migrate(
#     # migrator.alter_column_type(table='taka_crawler_record', column='ctime', field=DateTimeField()),
#     migrator.add_column('taka_crawler_record', 'description', CharField(default='xxx')),
#
# )

# Storing Data
# profile_record = TakaCrawlerRecord.create(profile_name='alisharajput_22',
#                                           craweld_publisher_id='xxxxxxxxx', status='pending')

# --------- Retrieving Data-----------
# get 只取一条数据，多条也只取第一条
one = TakaCrawlerRecord.get(TakaCrawlerRecord.profile_name == 'alisharajput_22')
print(one.profile_name, one.id)

# update
# one.profile_name = 'test_update'
# one.save()

# Lists of records
# query = TakaCrawlerRecord.select().where(TakaCrawlerRecord.profile_name == 'alisharajput_22')
# for obj in query:
#     print(obj.id, obj.profile_name)

# count
count = TakaCrawlerRecord.select().where(TakaCrawlerRecord.profile_name == 'alisharajput_22').count()
print(count)
# mysql_db.close()
db_pool.close()



