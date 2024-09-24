from .models import Category, SubCategory, ForumComments, Spot, Review
from rest_framework import serializers

# Creating Custom Serializers
# class CategorySerializers(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(max_length=300)
#     slug = serializers.CharField(required=False, allow_blank=True)

#     def create(self, validated_data):
#         '''
#             Validated_data is in form of dictionary
#         '''
#         return Category.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         ''' Get the updated values from the validated_data dictionary ,
#             if the field is not present in the dict then take the instance data itself then save and return
#         '''

#         instance.name = validated_data.get('name', instance.name)
#         instance.slug = validated_data.get('slug', instance.slug)
#         instance.save()
#         return instance
#     class Meta:
#         model = Category
#         fields = '__all__'


# Creating Model Serializers
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = '__all__'

class SubcategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

class SpotSerializers(serializers.ModelSerializer):
    # Can also add extra field or override default fields. Extra fields can correspond to any property or callable on the model.
    class Meta:
        model = Spot
        fields = ['id', 'name', 'city', 'description', 'uploaded_by', 'sub_category', 'updated_at', 'created_at','visited_users']