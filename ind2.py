#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариаент 18
# Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям магазинов; вывод на экран информации о товарах, продающихся в магазине,
# название которого введено с клавиатуры; если такого магазина нет, выдать на дисплей
# соответствующее сообщение.
#Выполнить индивидуальное задание 2 лабораторной работы 9, использовав классы данных, а
#также загрузку и сохранение данных в формат XML.



from dataclasses import dataclass, field
import sys
from typing import List
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class markets:
    shop: str
    product: str
    price: float


@dataclass
class Staff:
    market: List[markets] = field(default_factory=lambda: [])

    def add(self, shop, product, price):
        self.market.append(
            markets(
                shop=shop,
                product=product,
                price=price
            )
        )

        self.market.sort(key=lambda markets: markets.shop)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        table.append(line)
        table.append(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "No",
                "Продукт",
                "Магазин",
                "Цена"
            )
        )
        table.append(line)

        # Вывести данные о всех товарах.
        for idx, markets in enumerate(self.market, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    markets.shop,
                    markets.product,
                    markets.price
                )
            )
        table.append(line)

        return '\n'.join(table)

    def select(self, shop):
        parts = command.split(' ', maxsplit=1)
        shop = str(parts[1])
        count = 0
        result = []
        for markets in self.market:
            if product in markets.product:
                count += 1
                result.append(markets)
        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()

        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)

        self.market = []
        for markets_element in tree:
            shop, product, price = None, None, None
            for element in markets_element:
                if element.tag == 'shop':
                    shop = element.text
                elif element.tag == 'product':
                    product = element.text
                elif element.tag == 'price':
                    price = float(element.text)

                if shop is not None and product is not None \
                        and price is not None:
                    self.market.append(
                        markets(
                            shop=shop,
                            product=product,
                            price=price
                        )
                    )

    def save(self, filename):
        root = ET.Element('market')
        for markets in self.market:
            markets_element = ET.Element('markets')


            shop_element = ET.SubElement(markets_element, 'shop')
            shop_element.text = markets.shop

            product_element = ET.SubElement(markets_element, 'product')
            product_element.text = markets.product

            price_element = ET.SubElement(markets_element, 'price')
            price_element.text = str(markets.price)

            root.append(markets_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    # Список товара.
    staff = Staff()

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о товаре.
            product = str(input("Название товара? "))
            shop = input("Название магазина? ")
            price = float(input("Стоимость товара в руб.? "))

            # Добавить.
            staff.add(shop, product, price)

        elif command == 'list':
            # Вывести список.
            print(staff)

        elif command.startswith('select '):

            parts = command.split(maxsplit=1)
            # Запросить товар.
            selected = staff.select(parts[1])
            # Вывести результаты запроса.
            if selected:
                for count, markets in enumerate(selected, 1):
                    print(
                        '{:>4}: {}'.format(count, markets.shop)
                    )
            else:
                print("Магазин не найден.")

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)

            # Прочитать данные из файла.
            staff.load(parts[1])

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(maxsplit=1)
            # Сохранить данные в файл.
            staff.save(parts[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("select <товар> - информация о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
