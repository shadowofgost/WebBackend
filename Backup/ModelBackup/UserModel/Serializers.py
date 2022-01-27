
from django.forms import fields
from rest_framework import serializers
from .Database import UserModel, UserExtensionModel,DepartmentModel
class UserModelSerializer(serializers.ModelSerializer):
    department_name = serializers.SlugRelatedField(slug_field='name',source='deptid',queryset=DepartmentModel.objects.all())
    class Meta:
        model = UserModel
        exclude = ("back_up1","back_up2","back_up3","back_up4","back_up5","back_up6")

class UserExtensionModelSerializerIn(serializers.ModelSerializer):
    nouser = serializers.SlugRelatedField(slug_field='nouser',source='id_user',queryset=UserModel.objects.all())
    idmanager_nouser = serializers.SlugRelatedField(slug_field='nouser',source='idmanager',queryset=UserModel.objects.all())
    class Meta:
        model = UserExtensionModel
        exclude =("back_up1","back_up2","back_up3","back_up4","back_up5","back_up6")

class UserExtensionModelSerializerOut(UserExtensionModelSerializerIn):
    name = serializers.SlugRelatedField(slug_field='name',source='id_user',queryset=UserModel.objects.all())
    idmanager_name = serializers.SlugRelatedField(slug_field='name',source = "idmanager",queryset=UserModel.objects.all())
    class Meta(UserExtensionModelSerializerIn.Meta):
        exclude =("back_up1","back_up2","back_up3","back_up4","back_up5","back_up6")



class UserModelTotalSerializer(UserModelSerializer):

    class Meta(UserModelSerializer.Meta):
        exclude =("back_up1","back_up2","back_up3","back_up4","back_up5","back_up6")

