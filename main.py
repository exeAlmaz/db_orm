import sqlalchemy as sq
import os
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale
DSN = os.getenv('DSN')
engine = sq.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# //издатели//
pub_1 = Publisher(name='Пушкин')
pub_2 = Publisher(name='Есенин')
pub_3 = Publisher(name='Толстой')

session.add_all([pub_1, pub_2, pub_3])
session.commit()

# //книги//
bk_01 = Book(title='Капитанская дочка', publisher_id=pub_1.id)
bk_02 = Book(title='Руслан и Людмила', publisher_id=pub_1.id)
bk_03 = Book(title='Евгений Онегин', publisher_id=pub_1.id)
bk_04 = Book(title='Война и мир', publisher_id=pub_3.id)
bk_05 = Book(title='Собранине сочинений', publisher_id=pub_2.id)
bk_06 = Book(title='Анна Каренина', publisher_id=pub_3.id)
bk_07 = Book(title='Кавказский пленник', publisher_id=pub_3.id)


session.add_all([bk_01, bk_02, bk_03, bk_04, bk_05, bk_06, bk_07])
session.commit()

# //магазин//
sh_1 = Shop(name = 'Буквоед')
sh_2 = Shop(name = 'Книжный дом')
sh_3 = Shop(name = 'Лабиринт')

session.add_all([sh_1, sh_2, sh_3])
session.commit()


# //склад//
st_1 = Stock(id_book = bk_01.id , id_shop = sh_1.id , count = '10')
st_2 = Stock(id_book = bk_02.id , id_shop = sh_1.id , count = '8')
st_3 = Stock(id_book = bk_03.id , id_shop = sh_1.id , count = '20')
st_4 = Stock(id_book = bk_07.id , id_shop = sh_1.id, count = '20')
st_5 = Stock(id_book = bk_06.id , id_shop = sh_1.id , count = '15')

st_6 = Stock(id_book = bk_04.id , id_shop = sh_2.id, count = '11')
st_7 = Stock(id_book = bk_01.id , id_shop = sh_2.id, count = '13')
st_8 = Stock(id_book = bk_05.id , id_shop = sh_2.id, count = '16')

st_9 = Stock(id_book = bk_04.id , id_shop = sh_3.id , count = '16')
st_10 = Stock(id_book = bk_07.id , id_shop = sh_3.id , count = '13')
st_11 = Stock(id_book = bk_02.id , id_shop = sh_3.id , count = '5')
st_12 = Stock(id_book = bk_01.id , id_shop = sh_3.id , count = '3')

session.add_all([st_1, st_2, st_3, st_4, st_5, st_6, st_7, st_8, st_9, st_10, st_11, st_12])
session.commit()

# //Цена//
sl_1 = Sale(price = '200.00', date_sale = '2024-05-01', id_stock = st_1.id, count = '2')
sl_2 = Sale(price = '500.00', date_sale = '2024-05-03', id_stock = st_2.id, count = '2')
sl_3 = Sale(price = '300.00', date_sale = '2024-05-10', id_stock = st_3.id, count = '3')
sl_4 = Sale(price = '350.00', date_sale = '2024-05-12', id_stock = st_3.id, count = '4')
sl_5 = Sale(price = '400.00', date_sale = '2024-05-13', id_stock = st_4.id, count = '2')
sl_6 = Sale(price = '240.00', date_sale = '2024-05-04', id_stock = st_11.id, count = '2')
sl_7 = Sale(price = '200.00', date_sale = '2024-05-03', id_stock = st_5.id, count = '4')
sl_8 = Sale(price = '210.00', date_sale = '2024-05-02', id_stock = st_6.id, count = '2')
sl_9 = Sale(price = '240.00', date_sale = '2024-05-08', id_stock = st_7.id, count = '5')
sl_10 = Sale(price = '240.00', date_sale = '2024-05-04', id_stock = st_8.id, count = '6')
sl_11 = Sale(price = '210.00', date_sale = '2024-05-14', id_stock = st_9.id, count = '4')
sl_12 = Sale(price = '215.00', date_sale = '2024-05-18', id_stock = st_10.id, count = '4')
session.add_all([sl_1, sl_2, sl_3, sl_4, sl_5, sl_6, sl_7, sl_8, sl_9, sl_10, sl_11, sl_12])
session.commit()

print(sl_1.date_sale)

search = input('Напишите фамилию или id автора')
select = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)


if search.isdigit():
    select = select.filter(Publisher.id == search).all()
else:
    select = select.filter(Publisher.name == search).all()

for title, name, price, date_sale in select:
    print(f'{title} |  {name} | {price} | {date_sale}')


session.close()
