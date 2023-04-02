import random
import string

from faker import Faker

from basemod import MySQLConnection


fake = Faker()

def generate_product_list(n=1):
    def generate_product():
        return {
            "name": ' '.join(fake.words(nb=3)),
            "count": random.randint(1, 200),
            "value": random.randint(1, 10000),
        }

    return [generate_product() for _ in range(n)]

def main():
    connection = MySQLConnection(
        host="all-db",
        database="archdb",
        user="stud",
        password="stud"
    )

    connection.execute("""CREATE TABLE IF NOT EXISTS `Products` (
        `id`    INT NOT NULL AUTO_INCREMENT,
        `name`  VARCHAR(1024) NOT NULL,
        `count` INT NOT NULL,
        `value` INT NOT NULL,
        PRIMARY KEY (`id`), KEY `an` (`name`)
    );""")

    values = generate_product_list(200)
    connection.insert_values(("INSERT INTO `Products` "
        "(`name`, `count`, `value`) "
        "VALUES (%(name)s, %(count)s, %(value)s)"), values)

if __name__ == "__main__":
    main()
