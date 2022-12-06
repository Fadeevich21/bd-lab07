import peewee as pw
from .config import BaseModel


class LevelSettingDown(BaseModel):
    level_setting_down_id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=50)
    
    class Meta:
        db_table = 'levels_setting_down'

class Teacher(BaseModel):
    teacher_id = pw.IntegerField(primary_key=True)
    fcs = pw.CharField(max_length=100)
    level_setting_down = pw.ForeignKeyField(LevelSettingDown, null=False, backref='levels_setting_down')

    class Meta:
        db_table = 'teachers'

class Group(BaseModel):
    group_id = pw.IntegerField(primary_key=True)
    name = pw.CharField(10)

    class Meta:
        db_table = 'groups'

class Department(BaseModel):
    department_id = pw.IntegerField(primary_key=True)
    name = pw.CharField(70)

    class Meta:
        db_table = 'departments'

class DepartmentTeacher(BaseModel):
    department_id = pw.ForeignKeyField(Department, null=False, backref='departments')
    teacher_id = pw.ForeignKeyField(Teacher, null=False, backref='teachers')

    class Meta:
        primary_key = False
        db_table = 'departments_teachers'

class DepartmentGroup(BaseModel):
    department_id = pw.IntegerField(null=False)
    group_id = pw.ForeignKeyField(Group, null=False, backref='groups')

    class Meta:
        primary_key = False
        db_table = 'departments_groups'

class Discipline(BaseModel):
    discipline_id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=50)

    class Meta:
        db_table = 'disciplines'

class Parlour(BaseModel):
    parlour_id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=30)

    class Meta:
        db_table = 'parlours'

class Session(BaseModel):
    session_id = pw.IntegerField(primary_key=True)
    start_time = pw.TimeField()
    end_time = pw.TimeField()

    class Meta:
        db_table = 'sessions'

class Schedule(BaseModel):
    day_week = pw.CharField(max_length=20)
    session_id = pw.ForeignKeyField(Session, null=False, backref='sessions')
    discipline_id = pw.ForeignKeyField(Discipline, null=False, backref='disciplines')
    group_id = pw.ForeignKeyField(Group, null=False, backref='groups')
    teacher_id = pw.ForeignKeyField(Teacher, null=False, backref='teachers')
    parlour_id = pw.ForeignKeyField(Parlour, null=False, backref='parlours')

    class Meta:
        primary_key = False
        db_table = 'schedules'
