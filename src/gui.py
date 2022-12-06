from .menu import Menu
from . import query
import tkinter as tk
from tkinter import ttk


class Gui(tk.Frame):
    
    def __add_queries(self):
        for query_ in [query.QueryLevelsSettingDown(), query.QueryTeachers(),
                       query.QueryGroups(), query.QueryDepartments(),
                       query.QueryDepartmentsTeachers(), query.QuerySchedules(),
                       query.QueryDepartmentsGroups(), query.QueryDisciplines(),
                       query.QueryParlours(), query.QuerySessions()]:
            self.__menu.add_query(query_)

    def __init_main_workplace(self):
        self.main_workplace = tk.Frame()
        self.main_workplace.place(x=0, y=0, width=1000, height=600)

    def __init_combobox(self):
        self.__combobox = ttk.Combobox(self.main_workplace, values=self.__menu.get_list_names(), state="readonly", width=75, justify='center')
        self.__combobox.current(0)
        self.__combobox.place(x=390, y=475, width=200)

    def __init_btn_build(self):
        self.__btn_build = ttk.Button(self.main_workplace, text='Построить', command=self.show_table)
        self.__btn_build.place(x=442, y=525)

    def __init_widgets_show_table(self):
        self.__init_combobox()
        self.__init_btn_build()

    def __init__(self, root: tk.Tk) -> None:
        root.resizable(False, False)
        super().__init__(root)

        self.__init_main_workplace()
        self.__table: ttk.Treeview = None

        self.__menu = Menu()
        self.__add_queries()

        self.__init_widgets_show_table()


    def get_choose(self):
        choose_text = self.__combobox.get()
        choose = self.__menu.get_choose(choose_text)
        return choose


    def __remove_table_elements(self):
        if self.__table is not None:
            self.__table.destroy()
            self.__scroll_panel_x.destroy()
            self.__scroll_panel_y.destroy()


    def __show_scroll_panel_x(self):
        self.__scroll_panel_x = ttk.Scrollbar(self.main_workplace, command=self.__table.xview, orient='horizontal')
        self.__table.configure(xscrollcommand=self.__scroll_panel_x.set)
        self.__scroll_panel_x.place(x=20, y=320, width=950)

    def __show_scroll_panel_y(self):
        self.__scroll_panel_y = ttk.Scrollbar(self.main_workplace, command=self.__table.yview)
        self.__table.configure(yscrollcommand=self.__scroll_panel_y.set)
        self.__scroll_panel_y.place(x=970, y=20, height=300)

    def __show_scroll_panels(self):
        self.__show_scroll_panel_x()
        self.__show_scroll_panel_y()


    def __set_headers(self, headers: list) -> None:
        self.__table['columns'] = headers
        for header in headers:
            self.__table.heading(header, text=header, anchor='center')
            self.__table.column(header, anchor='center')


    def __insert_records_headers(self):
        choose = self.get_choose()
        records, headers = self.__menu.handle(choose)
        self.__set_headers(headers)
        for i in range(len(records)):
            record = records[i]
            if i % 2 == 0:
                self.__table.insert('', tk.END, values=record)
            else:
                self.__table.insert('', tk.END, values=record, tags='gray')
            self.__table.tag_configure('gray', background='#D3D3D3')

    def __init_table(self) -> None:
        self.__table = ttk.Treeview(self.main_workplace, show='headings')

        self.__insert_records_headers()


    def __show_table(self) -> None:
        self.__init_table()
        self.__table.place(x=20, y=20, width=950, height=301)

    def show_table(self):
        self.__remove_table_elements()
        self.__show_table()
        self.__show_scroll_panels()