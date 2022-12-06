from . import models
# from flask import jsonify
from .serializers import *


def where_filters(query, model: models.BaseModel, **filters):
    _filters = \
        [
            getattr(model, key) == value
            for key, value in filters.items() if value is not None
        ]
    if _filters:
        return query.where(*_filters)
    
    return query


def execute_get_all(model: models.BaseModel, serializer, **filters):
    query = model.select()
    query = where_filters(query, model, **filters)

    return [serializer(record) for record in query]

def get_levels_setting_down(**filters):
    return execute_get_all(models.LevelSettingDown, serialize_level_setting_down, **filters)

def get_teacher(**filters):
    return execute_get_all(models.Teacher, serialize_teacher, **filters)

def get_groups(**filters):
    return execute_get_all(models.Group, serialize_groups, **filters)

def get_departments(**filters):
    return execute_get_all(models.Department, serialize_departments, **filters)

def get_departments_teachers(**filters):
    return execute_get_all(models.DepartmentTeacher, serialize_departments_teachers, **filters)

def get_departments_groups(**filters):
    return execute_get_all(models.DepartmentGroup, serialize_departmnets_groups, **filters)

def get_disciplines(**filters):
    return execute_get_all(models.Discipline, serialize_disciplines, **filters)

def get_parlours(**filters):
    return execute_get_all(models.Parlour, serialize_parlours, **filters)

def get_sessions(**filters):
    return execute_get_all(models.Session, serialize_sessions, **filters)

def get_schedules(**filters):
    return execute_get_all(models.Schedule, serialize_schedules, **filters)
