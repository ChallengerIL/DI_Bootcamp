# 1. Using this API, create the functionality which will write 10 random countries to your database.

# 2. These are the attributes which you should populate your tables with: name, capital, flag, subregion, population.

import psycopg2
import requests
import random

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'countries'
TABLE_NAME = 'random_countries'


def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results


class Countries:

    def __init__(self, num):
        self.all_countries = requests.get("https://restcountries.com/v3.1/all").json()
        self.name = None
        self.capital = None
        self.flag = None
        self.subregion = None
        self.population = None

        for _ in range(num):
            self.get_country_data()
            self.save()

    def save(self):
        try:
            return run_query(
                f"INSERT INTO {TABLE_NAME}(name, capital, flag, subregion, population) "
                f"VALUES ('{self.name}', '{self.capital}', '{self.flag}', '{self.subregion}', {self.population}) "
                f"RETURNING country_id;")
        except psycopg2.errors.UniqueViolation:
            print("Country with the same name already exists in the table.")

    def get_country_data(self):
        while True:
            country = self.all_countries[random.randint(0, len(self.all_countries)-1)]
            try:
                self.name = country['name']['official']
                self.capital = country['capital'][0]
                self.flag = country['flag']
                self.subregion = country['subregion']
                self.population = country['population']
            except KeyError:
                continue
            else:
                break


if __name__ == '__main__':
    countries = Countries(10)
