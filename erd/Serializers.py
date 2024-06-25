from rest_framework import serializers
from .models import patient,Escort,Medicine,Diseases,Document,Reminder,Register
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=False)
    username = serializers.CharField(read_only=True)


    def create(self, validated_data):
        password=validated_data.pop('password')
        user =User.objects.create(**validated_data)
        user.save()

        return user

    class Meta:
        model=User
        fields=['url','id','username','email','first_name','last_name','password']



class RegisterSerializers(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True)

    class Meta:
        model = Register
        fields = [
            'name',
            'emaill',
            'Password',
            'RePassword',
            'PhoneNumber',
        ]

    def create(self, validated_data):
        password = validated_data.pop('Password', None)
        re_password = validated_data.pop('RePassword', None)
        if password != re_password:
            raise serializers.ValidationError("Passwords do not match.")
        
        register_instance = Register.objects.create(**validated_data)
        if password:
            register_instance.Password = password  # You might need to hash the password here if necessary
        register_instance.save()
        return register_instance



# class LoginSerializers(serializers.ModelSerializer):
#     class Meta:
#         model= Login 
#         fields="__all__"

class pSerializers(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = patient
        fields = [
            'FirstName',
            'LasttName',
            'patientID',
            'EscortID',
            'DiseaseID',
            'Email',
            'Password', 
            'PhoneNumber',
            'Handel',
            'ProfilePicture',
            'Male',
            'Female',
        ]

    def create(self, validated_data):
        password = validated_data.pop('Password', None)
        patient_instance = patient.objects.create(**validated_data)
        if password:
            patient_instance.Password = password  # You might need to hash the password here if it's a custom user model
        patient_instance.save()
        return patient_instance




class ESerializers(serializers.ModelSerializer):
    Password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Escort
        fields = [
            'FirstName',
            'LasttName',
            'EscortID',
            'Email',
            'Password',  # Ensure Password is included here
            'PhoneNumber',
            'yourHandel',
            'ProfilePicture',
            'Male',
            'Female',
            'LastModified'
        ]

    def create(self, validated_data):
        password = validated_data.pop('Password', None)
        escort = Escort.objects.create(**validated_data)
        if password:
            escort.Password = password  # You might need to hash the password here if it's a custom user model
        escort.save()
        return escort



class DSerializers(serializers.ModelSerializer):
    class Meta:
        model= Diseases
        fields="__all__"


class MSerializers(serializers.ModelSerializer):
    class Meta:
        model= Medicine
        fields="__all__"


class DOSerializers(serializers.ModelSerializer):
    class Meta:
        model= Document
        fields="__all__"


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reminder
        fields =['ReminderID', 'patientID', 'StartDate', 'EndDate', 'State', 'AlarmRecordes', 'Audio', 'Notes', 'PillCount', 'Checked']
