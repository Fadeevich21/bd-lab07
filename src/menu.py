from .config import db
from .query import Query
from typing import List, Tuple


class Menu:

    def __init__(self) -> None:
        self.__db = db
        self.__query = {}
        self.__menu = list()

    def get_list_names(self) -> List[str]:
        return list(self.__query.values())

    def add_query(self, query: Query):
        self.__query[len(self.__query)] = query.name()
        self.__menu.append(query)

    def get_choose(self, text_choose: str) -> int:
        for k, v in self.__query.items():
            if v == text_choose:
                return int(k)

    def handle(self, choose: int) -> Tuple[List[str], List[str]]:
        if choose > len(self.__menu):
            raise IndexError(f'Ваш выбор {choose} не допустим')

        res = self.__menu[choose].get_res()
        rows = [list(record.values()) for record in res]
        columns = list(res[0].keys())
        
        return (rows, columns)