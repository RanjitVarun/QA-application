from rest_framework import serializers
import user.models as models
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate

class EmailSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Email       
        fields = "__all__"

class MobileSerializer(serializers.ModelSerializer):    
    class Meta:        
        model = models.Mobile        
        fields = "__all__"

class ResAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.ResAddress     
        fields = "__all__"
            
class OffAddressSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.OfficeAddress     
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Education     
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Course     
        fields = ("course","degree_id")        
        
class BoardSerializer(serializers.ModelSerializer):    
    class Meta:        
        model =   models.Board     
        fields ="__all__"

class BoardCourseSerializer(serializers.Serializer):
    board = BoardSerializer(many=True, read_only=True)
    course = CourseSerializer(many=True, read_only=True)
    degree= EducationSerializer(many=True, read_only=True)
    class Meta:          
        fields = "__all__"        
     
class EduRelSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   models.EducationRelUser    
        fields = ("course","board","degree")  
        depth = 1 

class SkillSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   models.Skillset    
        fields = "__all__"

class SkillsetSerializer(serializers.ModelSerializer):
    skill=SkillSerializer(many=True, read_only=True) 
    class Meta:        
        model =   models.skillsetRel    
        fields = "__all__"
    
class SkillsetRelSerializer(serializers.ModelSerializer):
    skill=SkillSerializer(many=True, read_only=True) 
    class Meta:        
        model =   models.skillsetRel    
        fields = "__all__" 
        depth=1   

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:        
        model =   models.UserDetails   
        fields = "__all__" 

class UserSerializer(serializers.ModelSerializer):
   email = EmailSerializer(many=True, read_only=True)   
   mobile =MobileSerializer(many=True, read_only=True)  
   resaddress =ResAddressSerializer(many=True, read_only=True) 
   offaddress =OffAddressSerializer(many=True, read_only=True)
   user_relation=EduRelSerializer(many=True, read_only=True)
   user_skill=SkillsetRelSerializer(many=True, read_only=True)
  
   class Meta:
        fields = (
            'id',
            'first_name',
            'last_name',
            'DOB',
            'gender',
            'password', 
            'email',
            'mobile',
            'resaddress',
            'offaddress',
            'user_relation', 
            'user_skill',
        )
        model = models.UserDetails
       

class UserSerializerWithToken(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
    JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

    def validate(self, data):
        print("validate")
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            print("user if")
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }











    # def get_token(self, obj):
    #     jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    #     jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    #     payload = jwt_payload_handler(obj)
    #     token = jwt_encode_handler(payload)
    #     return token

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance

    # class Meta:
    #     model = models.UserDetails
    #     fields = ('token', 'first_name', 'password')
     