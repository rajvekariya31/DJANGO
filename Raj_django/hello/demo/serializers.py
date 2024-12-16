from rest_framework import serializers
from.models import *

class studserializer(serializers.ModelSerializer):
    class Meta:
        model=stud
        fields= "__all__"
        
    def validate(self,data):
        
        # #validations
        
        #number 
        
        mob = data.get('number')
        if len(mob) != 10 or not mob.isdigit():
            raise serializers.ValidationError('enter only number:')

        #name
        
        if not data['name'].isalpha():
            raise serializers.ValidationError('enter only alph:')
          
        #age 
         
        if data["age"] < 18:
            raise serializers.ValidationError("user must has been 18 or 18+")
          
        #email
          
        email = data.get('email') 
        if data['email'] == '@gmail.com':
           raise serializers.ValidationError("email is not valide")
       
        elif email[0].isdigit():
           raise serializers.ValidationError("email is not valide")
       
        elif not email.islower():
            raise serializers.ValidationError("email is not valide")
        
        elif not email.endswith('@gmail.com'):
           raise serializers.ValidationError("email is not valide")
        
        #pass
        
        if data['password'] != data['cpass'] :
            raise serializers.ValidationError("password not matched")
        
        return data