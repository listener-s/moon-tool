import shortuuid
from django.db import models


def create_uuid():
    uuid = shortuuid.uuid()
    return uuid


class BaseModel(models.Model):
    DEL_STATUS = ((0, '已删除'), (1, '默认'))
    uuid = models.CharField('ID', max_length=255, primary_key=True, default=create_uuid, editable=False)
    add_time = models.DateTimeField('创建时间', auto_now_add=True)
    del_state = models.IntegerField('删除状态', choices=DEL_STATUS, default=1, db_index=True)

    class Meta:
        abstract = True  # 定义抽象类
        db_table = 'Base'  # 定义表名
