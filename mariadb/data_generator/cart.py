import random
import string

from faker import Faker

from basemod import MySQLConnection


fake = Faker()

def flatten(l):
    return [item for sublist in l for item in sublist]

def get_unique_ids(table):
    connection = MySQLConnection(
        host="all-db",
        database="archdb",
        user="stud",
        password="stud"
    )
    ids_list = connection.get(f"SELECT id FROM {table.title()};")
    ids_list = list(map(lambda x : x[0], ids_list))
    print(ids_list)
    return ids_list

def generate_cart_list(n=1):
    user_ids = get_unique_ids('user')
    product_ids = get_unique_ids('products')

    n = min(n, len(user_ids))

    def generate_cart_entries(user_id):
        cart_size = random.randrange(len(product_ids))
        entries = random.choices(product_ids, k=cart_size)

        return [{"user_id": user_id, "product_id": pi} for pi in entries]

    return flatten([generate_cart_entries(i) for i in range(n)])

def main():
    connection = MySQLConnection(
        host="all-db",
        database="archdb",
        user="stud",
        password="stud"
    )

    connection.execute("""CREATE TABLE IF NOT EXISTS `Carts` (
    `id`         INT NOT NULL AUTO_INCREMENT,
    `user_id`    INT NOT NULL,
    `product_id` INT NOT NULL,
    PRIMARY KEY (`id`), KEY `uid` (`user_id`)
    );""")

    values = generate_cart_list(200)
    connection.insert_values(("INSERT INTO `Carts` "
        "(`user_id`, `product_id`) "
        "VALUES (%(user_id)s, %(product_id)s)"), values)

if __name__ == "__main__":
    main()
