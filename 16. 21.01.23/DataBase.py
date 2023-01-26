from Person import Person
from Number import Number
from Address import Address
import datetime as dt


class DataBase:
    person_table: list[Person]
    number_table: list[Number]
    address_table: list[Address]

    def __init__(self) -> None:
        self.person_table = []
        self.number_table = []
        self.address_table = []

    def append_person(self, person: Person) -> None:
        self.person_table.append(person)
        self.sort_table(self.person_table)

    def append_number(self, number: Number) -> None:
        self.number_table.append(number)
        self.sort_table(self.number_table)

    def append_address(self, address: Address) -> None:
        self.address_table.append(address)
        self.sort_table(self.address_table)

    def remove_person(self, person_id: int) -> None:
        for p in self.person_table:
            if p.id == person_id:
                self.person_table.remove(p)

    def remove_number(self, number_id: int) -> None:
        for n in self.number_table:
            if n.id == number_id:
                self.number_table.remove(n)

    def remove_address(self, address_id: int) -> None:
        for a in self.address_table:
            if a.id == address_id:
                self.address_table.remove(a)

    def update_person(self, person: Person) -> None:
        for id, p in enumerate(self.person_table):
            if p.id == person.id:
                self.person_table[id] = person

    def update_number(self, number: Number) -> None:
        for id, n in enumerate(self.number_table):
            if n.id == number.id:
                self.number_table[id] = number

    def update_address(self, address: Address) -> None:
        for id, a in enumerate(self.number_table):
            if a.id == address.id:
                self.address_table[id] = address

    def search_person(self, criteria: int, key: str, mode: int) -> str:
        output = ""
        if criteria == 1:
            key = int(key)
        elif criteria == 3:
            list_key = list(map(int, key.split("-")))
            key = dt.date(list_key[0], list_key[1], list_key[2])
        data = [list(person.export_data().values()) for person in self.person_table]
        for i, person in enumerate(data):
            for j, value in enumerate(person):
                if j == criteria - 1:
                    if j == 2:
                        list_value = list(map(int, value.split("-")))
                        value = dt.date(list_value[0], list_value[1], list_value[2])
                    if (mode == 0 or mode == 3) and key == value:
                        output += f'{self.person_table[i]}\n'
                    elif mode == 1 and key <= value:
                        output += f'{self.person_table[i]}\n'
                    elif mode == 2 and key >= value:
                        output += f'{self.person_table[i]}\n'
        return output

    def search_number(self, criteria: int, key: str, mode: int) -> str:
        output = ""
        if criteria != 4:
            key = int(key)
        data = [list(number.export_data().values()) for number in self.number_table]
        for i, number in enumerate(data):
            for j, value in enumerate(number):
                if j == criteria - 1:
                    if (mode == 0 or mode == 3) and key == value:
                        output += f'{self.number_table[i]}\n'
                    elif mode == 1 and key <= value:
                        output += f'{self.number_table[i]}\n'
                    elif mode == 2 and key >= value:
                        output += f'{self.number_table[i]}\n'
        return output

    def search_address(self, criteria: int, key: str, mode: int) -> str:
        output = ""
        if criteria == 1 or criteria == 2:
            key = int(key)
        data = [list(address.export_data().values()) for address in self.address_table]
        for i, address in enumerate(data):
            for j, value in enumerate(address):
                if j == criteria - 1:
                    if (mode == 0 or mode == 3) and key == value:
                        output += f'{self.address_table[i]}\n'
                    elif mode == 1 and key <= value:
                        output += f'{self.address_table[i]}\n'
                    elif mode == 2 and key >= value:
                        output += f'{self.address_table[i]}\n'
        return output

    def sort_table(self, table: list) -> None:
        size = len(table)
        for i in range(size):
            min_index = i
            for j in range(i + 1, size):
                if table[j].id < table[min_index].id:
                    min_index = j
            table[i], table[min_index] = table[min_index], table[i]

    def select_table(self, table: int) -> str:
        output: str = ""

        if table == 1:
            for p in self.person_table:
                output += f'{p}\n'
        if table == 2:
            for n in self.number_table:
                output += f'{n}\n'
        if table == 3:
            for a in self.address_table:
                output += f'{a}\n'

        return output

    def export_data(self) -> dict:
        output: dict = {"people": [person.export_data() for person in self.person_table], "numbers": [number.export_data() for number in self.number_table], "addresses": [address.export_data() for address in self.address_table]}
        return output
