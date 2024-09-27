from .models import Category, SubCategory, ForumComments, Spot, Review
from rest_framework import serializers

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
            model = Category
            fields = ['id', 'name']
    
    def validate_name(self, value):
        normalized_value = ''.join(value.split()).lower()

        for category in Category.objects.all():
            normalized_existing_name = ''.join(category.name.split()).lower()
            if normalized_existing_name == normalized_value:
                raise serializers.ValidationError("Category with this name already exists")
        return value

class SubcategorySerializers(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'name','category_id','category_name']

    def validate_name(self, value):
        normalized_value = ''.join(value.split()).lower()

        for category in SubCategory.objects.all():
            normalized_existing_name = ''.join(category.name.split()).lower()
            if normalized_existing_name == normalized_value:
                raise serializers.ValidationError("SubCategory with this name already exists")
        return value

class SpotSerializers(serializers.ModelSerializer):
    posted_by = serializers.SerializerMethodField()
    class Meta:
        model = Spot
        fields = ['id', 'name', 'city', 'description', 'average_rating', 'sub_category','posted_by', 'updated_at', 'created_at', 'visited_users']
    
    def get_posted_by(self, obj):
        return obj.uploaded_by.username
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sub_category'] = {
            'id': instance.sub_category.id,
            'name': instance.sub_category.name
        }
        representation['category'] = instance.sub_category.category.name
        return representation
    
class ReviewSerializers(serializers.ModelSerializer):
    reviewed_by = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ['rating', 'review_text', 'reviewed_by']
    def get_reviewed_by(self, obj):
        return obj.user.username
    
    def validate_rating(self, value):
        if value not in range(1,6):
            raise serializers.ValidationError("Rating must between 1 to 5")
        return value

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumComments
        exclude = ['id']