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
class Employee(models.Model):
    emp_no = models.CharField(primary_key=True, max_length=10)
    surname = models.CharField(max_length=50, blank=True, null=True)
    o_name = models.CharField(max_length=50, blank=True, null=True)
    branch = models.CharField(max_length=10, blank=True, null=True)
    town = models.CharField(max_length=10, blank=True, null=True)
    dept = models.CharField(max_length=10, blank=True, null=True)
    sub_dept = models.CharField(max_length=10, blank=True, null=True)
    job_desc = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    scan_code = models.CharField(max_length=50, blank=True, null=True)
    working_hours = models.CharField(max_length=10, blank=True, null=True)
    bfwd = models.CharField(max_length=50, blank=True, null=True)
    emp_union = models.BooleanField(blank=True, null=True)
    remuneration = models.CharField(max_length=10, blank=True, null=True)
    leave_days = models.CharField(max_length=10, blank=True, null=True)
    shift = models.CharField(max_length=10, blank=True, null=True)
    deny_ot = models.CharField(max_length=10, blank=True, null=True)
    employee_type = models.CharField(max_length=10, blank=True, null=True)
    engage_date = models.DateField(blank=True, null=True)
    payment_mode = models.CharField(max_length=10, blank=True, null=True)
    bank_code = models.CharField(max_length=10, blank=True, null=True)
    bank_branch = models.CharField(max_length=10, blank=True, null=True)
    bank_name = models.CharField(max_length=10, blank=True, null=True)
    kra_pin = models.CharField(max_length=15, blank=True, null=True)
    paye = models.BooleanField(blank=True, null=True)
    nssf = models.BooleanField(blank=True, null=True)
    nssf_no = models.CharField(max_length=10, blank=True, null=True)
    vol_nssf = models.CharField(max_length=50, blank=True, null=True)
    nhif = models.BooleanField(blank=True, null=True)
    nhif_no = models.CharField(max_length=10, blank=True, null=True)
    perf_relief = models.CharField(max_length=10, blank=True, null=True)
    bfwd_relief = models.CharField(max_length=10, blank=True, null=True)
    ins_relief = models.CharField(max_length=10, blank=True, null=True)
    input_by = models.CharField(max_length=15, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    edit_by = models.CharField(max_length=15, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    leave_td = models.CharField(max_length=50, blank=True, null=True)
    leave_bf = models.CharField(max_length=50, blank=True, null=True)
    leave_os = models.CharField(max_length=50, blank=True, null=True)
    id_no = models.CharField(max_length=10, blank=True, null=True)
    bank_acc_name = models.CharField(max_length=50, blank=True, null=True)
    branch_code = models.CharField(max_length=10, blank=True, null=True)
    cheque_name = models.CharField(max_length=50, blank=True, null=True)
    bank_acc = models.CharField(max_length=20, blank=True, null=True)
    termination_date = models.DateField(blank=True, null=True)
    faceimage = models.TextField(blank=True, null=True)
    passport = models.TextField(blank=True, null=True)
    fingerprints = models.TextField(blank=True, null=True)
    current_shift = models.CharField(max_length=10, blank=True, null=True)
    prd_allocated = models.BooleanField(blank=True, null=True)
    prd_code = models.CharField(max_length=10, blank=True, null=True)
    prd_alloc_date = models.DateField(blank=True, null=True)
    current_batch = models.CharField(max_length=10, blank=True, null=True)
    shift_group_allocated = models.BooleanField(blank=True, null=True)
    clockin_date = models.DateTimeField(blank=True, null=True)
    has_clockedin = models.BooleanField(blank=True, null=True)
    is_sys_user = models.BooleanField(blank=True, null=True)
    run_date = models.CharField(max_length=30, blank=True, null=True)
    prd_sect_alloc_date = models.DateField(blank=True, null=True)
    prd_sect_code = models.CharField(max_length=30, blank=True, null=True)
    prd_sect_allocated = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


