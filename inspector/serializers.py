from .models import Inspection, InsGrading, InsSummary
from rest_framework import serializers


class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = ('code', 'name', 'compulsary', 'notes',
                  'input_by', 'input_date', 'edit_by', 'edit_date')


class InsGradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsGrading
        fields = ('code', 'description', 'startpoint', 'endpoint', 'comment',
                  'qualified', 'input_by', 'input_date', 'edit_by', 'edit_date')


class InsSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = InsSummary
        fields = ('doc_no', 'emp_no', 'emp_name', 'ins_date', 'total', 'score', 'ins_grade',
                  'passed', 'insp_comment', 'input_by', 'input_date', 'edit_by', 'edit_date')
