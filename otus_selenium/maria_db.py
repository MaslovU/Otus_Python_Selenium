"""Maria DB"""

from otus_selenium.DBcm import UseDatabase

dbconfig = {'host': 'localhost',
            'user': 'maslov',
            'password': 'my_passwd',
            'database': 'opencart'}


def maria_db_create_product_table():
    """Create table"""
    # Create new table
    with UseDatabase(dbconfig) as cursor:
        cursor.execute('''CREATE TABLE product_table
                        (id int auto_increment primary key,
                        ts timestamp default current_timestamp,
                        product_name varchar(128) not null,
                        price int not null)''')


def add_new_item_to_db(product_name, price):
    """Add items"""
    with UseDatabase(dbconfig) as cursor:

        _SQL = """INSERT INTO product_table
                (product_name, price)
                VALUES
                (%s, %s)"""

        cursor.execute(_SQL, (product_name, price,))


def chek_adding_to_db():
    """Check adding"""
    with UseDatabase(dbconfig) as cursor:
        cursor.execute('''SELECT * FROM product_table''')
        result = cursor.fetchall()
        # for i in result:
        #     print(i)
        to_check = result[2]
        print(to_check)
        assert 'iPhone 8' in to_check


# maria_db_create_product_table()
# add_new_item_to_db('iPhone 6', 10)
# add_new_item_to_db('iPhone 6+', 15)
# add_new_item_to_db('iPhone 8', 22)
# add_new_item_to_db('iPhone RS+', 100)
# add_new_item_to_db('Android 6', 11)
# add_new_item_to_db('Android 6+', 12)
# add_new_item_to_db('Android 8', 24)
# add_new_item_to_db('Android S+', 99)
chek_adding_to_db()


