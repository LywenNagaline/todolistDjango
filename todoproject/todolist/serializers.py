from rest_framework import serializers
from todolist.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'deadline', 'done')

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    deadline = serializers.DateField(required=False)
    done = serializers.BooleanField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.deadline = validated_data.get('deadline', instance.deadline)
        instance.done = validated_data.get('done', instance.done)
        instance.save()
        return instance