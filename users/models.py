from django.db import models


class SysUser(models.Model):
    user_code = models.CharField(primary_key=True, max_length=10)
    username = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50, blank=True, null=True)
    domain = models.CharField(max_length=50, blank=True, null=True)
    state = models.BooleanField(blank=True, null=True)
    user_no = models.CharField(max_length=10, blank=True, null=True)
    branch = models.CharField(max_length=10, blank=True, null=True)
    scan_code = models.CharField(max_length=10)
    oparator_code = models.CharField(max_length=10)
    user_group_alloc = models.BooleanField(blank=True, null=True)
    user_group = models.CharField(max_length=10, blank=True, null=True)
    input_by = models.CharField(max_length=15, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    edit_by = models.CharField(max_length=15, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    pass_dp = models.TextField(blank=True, null=True)
    pass_dp_len = models.SmallIntegerField(blank=True, null=True)
    pass_md5 = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'
