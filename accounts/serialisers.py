from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(User.objects.all())])
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    '''we can define first_name and last_name here. but i prefer to define these in extera_kwargs'''

    # first_name = serializers.CharField(required=False)
    # last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', 'first_name', 'last_name')
        ''' we can remove extra_kwargs and define first_name and last_name top of Meta class'''
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            # 'password1': {'required': True},
            # 'password2': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({
                'password': 'passwords does not match.'
            })
        return super(RegisterSerializer, self).validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            password=validated_data['password1']
        )

        ''' if we used User.objects.create , we have to use below lines
            to convert raw password to hash and we need to remove password from create method. 
            but if we use User.objects.create_user, it's no longer neeeded to define below lines.
        '''
        # user.set_password(validated_data['password1'])
        # user.save()
        return user
