from . import models


def serialize_level_setting_down(model: models.LevelSettingDown):
    return \
    {
        'id': model.level_setting_down_id,
        'name': model.name
    }

def serialize_teacher(model: models.Teacher):
    return \
    {
        'id': model.teacher_id,
        'fcs': model.fcs,
        'level setting down': model.level_setting_down
    }

def serialize_groups(model: models.Group):
    return \
    {
        'id': model.group_id,
        'name': model.name
    }

def serialize_departments(model: models.Department):
    return \
    {
        'id': model.department_id,
        'name': model.name
    }

def serialize_departments_teachers(model: models.DepartmentTeacher):
    return \
    {
        'department id': model.department_id,
        'teacher id': model.teacher_id
    }

def serialize_departmnets_groups(model: models.DepartmentGroup):
    return \
    {
        'department id': model.department_id,
        'group id': model.group_id
    }

def serialize_disciplines(model: models.Discipline):
    return \
    {
        'id': model.discipline_id,
        'name': model.name
    }

def serialize_parlours(model: models.Parlour):
    return \
    {
        'id': model.parlour_id,
        'name': model.name
    }

def serialize_sessions(model: models.Session):
    return \
    {
        'id': model.session_id,
        'start time': model.start_time,
        'end time': model.end_time
    }

def serialize_schedules(model: models.Schedule):
    return \
    {
        'day week': model.day_week,
        'session id': model.session_id,
        'discipline id': model.discipline_id,
        'group id': model.group_id,
        'teacher id': model.teacher_id,
        'parlour id': model.parlour_id
    }