from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer): # 그냥 Serializer은 유저가 따로 입력값을 만들 수 있음, ModelSerializer은 모델 내용을 그대로 반환함
    class Meta:
        model = Task # 모델가져오기
        fields = '__all__' # 모든 필드

    # def create(self, validated_data): # save()시 호출
    #     return Task.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.email = validated_data.get('title', instance.email)
    #     instance.date = validated_data.get('date', instance.date)
