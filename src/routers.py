from flask import request
from . import services


def post_levels_setting_down():
    if request.is_json:
        return services.create_levels_setting_down(request.get_json())
    return {}

def get_levels_setting_down():
    return services.get_levels_setting_down()

def get_level_setting_down_detail(pk: int):
    return services.get_level_setting_down_detail(pk)