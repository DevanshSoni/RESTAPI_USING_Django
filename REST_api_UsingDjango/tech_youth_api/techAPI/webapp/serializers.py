from rest_framework import serializers
from . userModel import *
from . interestModel import *


    #def __str__(self):
    #    return f"{instance.emailid}"

class interestSerializer(serializers.ModelSerializer):

    class Meta:
        model=interest
        fields='__all__'
        # fields = [
        #         'id',
        #         'question',
        #         ]
        # read_only_fields = ('question',)
        # depth=2

    def update(self, validated_data):
        instance = user.objects.get(temp_id=validated_data.get('temp_id'))
        # print(instance)
        # instance.usernamec  = validated_data.get('username')
        instance.interest = validated_data.get('InterestArea')

        instance.save()
        return instance


# class questionsSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=questions
#         fields='__all__'

#     def update(self, validated_data):
#         iid = user.objects.get(iid=validated_data.get('iid')) #interest id
#         instance.question = validated_data.get('question')
#         instance.save()
#         return instance


class userSerializer(serializers.ModelSerializer):
    interest = interestSerializer(many=True)

    class Meta:
        model=user
        fields='__all__'#['userid','username','password','emailid']#,'interest']



    def update(self, validated_data):
        instance = user.objects.get(user_id=validated_data.get('user_id'))
        # print(instance)
        instance.emailid=validated_data('emailid')
        instance.username = validated_data.get('username')
        instance.password = validated_data.get('password')
        instance.save()
        return instance

#
# class allSerializer(serializers.ModelSerializer):
#     # us = userSerializer(many=True)
#     # inter = interestSerializer(many=True)
#     # ques = questionsSerializer(many=True)
#
#     class Meta:
#         model=user,interest
#         fields =[{user:['username','password','emailid'],
#                     interest:['__all__']}]
