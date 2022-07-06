from .common import *
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    """
    REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'common.exceptions.custom_exception_handler',
    }
    """
    response = exception_handler(exc, context)  # 获取本来应该返回的exception的response
    if response is not None:
        response.data['status_code'] = response.status_code
        for exces in response.data:
            if isinstance(response.data.get(exces), list):
                response.data.get(exces)[0] = Common.chinese_translate(response.data.get(exces)[0])
    print('中文报错：', Common.chinese_translate(str(exc)))
    return response
