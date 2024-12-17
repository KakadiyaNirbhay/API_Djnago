from rest_framework import serializers
from .models import*  #import models



class studentserializer(serializers.ModelSerializer):  #crate class
    class Meta: #crate Meta class 
        model = student    #import models class name
        fields = '__all__'  #import models fields all
        
    # velidetion
    def validate(self,data):
        
        # name velidetion
        if not data["name"].isalpha():
            raise serializers.ValidationError("Name must contain only latters.")
        
        # age velidetion
        if data['age'] <18:
            raise serializers.ValidationError('The person has to be at least 18 years old.')
        
        
        # Email validation  
        emaill=data.get('email')
        if data["email"] == '@gmail.com':
            raise serializers.ValidationError('email is not valid')
        
        elif emaill[0].isdigit():
            raise serializers.ValidationError('email is not valid')
        
        elif not emaill.islower():
            raise serializers.ValidationError('email is not valid')
        
        elif not emaill.endswith('@gmail.com'):
            raise serializers.ValidationError('email is not valid')
        
        
        # mobile number velidation
        mobile=data.get('number')
        if len(mobile) != 10 or not mobile.isdigit():
            raise serializers.ValidationError('number is not validation')
        
        
        # password velidation
        if data['password'] != data['confirmpassword']:
            raise serializers.ValidationError('password is worng')
        
        
        return data

# class studentserializer1(serializers.ModelSerializer):
#     class Meta:
#         model = student1
#         fields = '__all__'
              