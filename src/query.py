from . import services
from . import models
from abc import ABC, abstractmethod

class Query(ABC):

    def __init__(self, name_table: str) -> None:
        self.__name_table = name_table

    def name(self) -> str:
        return self.__name_table

    @abstractmethod
    def get_res(self):
        pass


class QueryLevelsSettingDown(Query):

    def __init__(self) -> None:
        super().__init__('Levels setting down')

    def get_res(self):
        return services.get_levels_setting_down()

class QueryTeachers(Query):

    def __init__(self) -> None:
        super().__init__('Teachers')

    def get_res(self):
        return services.get_teacher()

class QueryGroups(Query):

    def __init__(self) -> None:
        super().__init__('Groups')

    def get_res(self):
        return services.get_groups()

class QueryDepartments(Query):

    def __init__(self) -> None:
        super().__init__('Departments')

    def get_res(self):
        return services.get_departments()

class QueryDepartmentsTeachers(Query):

    def __init__(self) -> None:
        super().__init__('Departments-Teachers')

    def get_res(self):
        return services.get_departments_teachers()

class QueryDepartmentsGroups(Query):

    def __init__(self) -> None:
        super().__init__('Departments-Groups')

    def get_res(self):
        return services.get_departments_groups()

class QueryDisciplines(Query):

    def __init__(self) -> None:
        super().__init__('Disciplines')

    def get_res(self):
        return services.get_disciplines()

class QueryParlours(Query):

    def __init__(self) -> None:
        super().__init__('Parlours')

    def get_res(self):
        return services.get_parlours()

class QuerySessions(Query):

    def __init__(self) -> None:
        super().__init__('Sessions')

    def get_res(self):
        return services.get_sessions()

class QuerySchedules(Query):

    def __init__(self) -> None:
        super().__init__('Schedules')

    def get_res(self):
        return services.get_schedules()
