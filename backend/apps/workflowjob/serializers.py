from rest_framework import serializers
from apps.workflowjob.models import JobType, JobRecord, JobCustomField, JobFlowLog, JobStateLastMan
from apps.workflow.models import Workflow


class JobTypeSerializer(serializers.ModelSerializer):
    gmt_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    gmt_modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    parent_type = serializers.SerializerMethodField()
    workflow = serializers.SerializerMethodField()

    class Meta:
        model = JobType
        exclude = ('parent_type_id', 'workflow_id')

    def get_parent_type(self, obj):
        if obj.parent_type_id:
            result = JobType.objects.filter(id=obj.parent_type_id, is_deleted=0).first()
            return dict(id=result.id, name=result.name)
        return dict()

    def get_workflow(self, obj):
        """
        获取流程信息
        :param obj:
        :return:
        """
        if obj.workflow_id:
            result = Workflow.objects.filter(id=obj.workflow_id, is_deleted=0).first()
            return dict(id=result.id, name=result.name)
        return dict()


class FormatJobTypeSerializer(serializers.ModelSerializer):
    gmt_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    gmt_modified = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    parent_type = serializers.SerializerMethodField()
    workflow = serializers.SerializerMethodField()
    format_name = serializers.SerializerMethodField()

    class Meta:
        model = JobType
        exclude = ('parent_type_id', 'workflow_id')

    def get_parent_type(self, obj):
        if obj.parent_type_id:
            result = JobType.objects.filter(id=obj.parent_type_id, is_deleted=0).first()
            return dict(id=result.id, name=result.name)
        return dict()

    def get_workflow(self, obj):
        """
        获取流程信息
        :param obj:
        :return:
        """
        if obj.workflow_id:
            result = Workflow.objects.filter(id=obj.workflow_id, is_deleted=0).first()
            return dict(id=result.id, name=result.name)
        return dict()

    def get_format_name(self, obj):
        """
        格式化的类型名称
        :param obj:
        :return:
        """
        return obj.format_name
