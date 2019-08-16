from django.db import models

# Create your models here.


class InsGrading(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    description = models.CharField(max_length=10, blank=True, null=True)
    startpoint = models.FloatField(blank=True, null=True)
    endpoint = models.FloatField(blank=True, null=True)
    comment = models.CharField(max_length=50, blank=True, null=True)
    qualified = models.BooleanField(blank=True, null=True)
    input_by = models.CharField(max_length=15, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    edit_by = models.CharField(max_length=15, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_grading'


class InsSummary(models.Model):
    doc_no = models.CharField(primary_key=True, max_length=10)
    emp_no = models.CharField(max_length=10, blank=True, null=True)
    emp_name = models.CharField(max_length=50, blank=True, null=True)
    ins_date = models.DateField(blank=True, null=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    score = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    ins_grade = models.CharField(max_length=20, blank=True, null=True)
    input_by = models.CharField(max_length=30, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    edit_by = models.CharField(max_length=15, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)
    run_date = models.CharField(max_length=10, blank=True, null=True)
    passed = models.DecimalField(
        max_digits=10, decimal_places=0, blank=True, null=True)
    insp_comment = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ins_summary'


class Inspection(models.Model):
    code = models.CharField(primary_key=True, max_length=3)
    name = models.CharField(max_length=50, blank=True, null=True)
    compulsary = models.BooleanField(blank=True, null=True)
    notes = models.CharField(max_length=50, blank=True, null=True)
    input_by = models.CharField(max_length=15, blank=True, null=True)
    input_date = models.DateTimeField(blank=True, null=True)
    edit_by = models.CharField(max_length=15, blank=True, null=True)
    edit_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inspection'
