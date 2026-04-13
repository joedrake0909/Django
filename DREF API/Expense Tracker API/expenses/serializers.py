from rest_framework import serializers
from .models import Transaction, Category







class CategorySerializer(serializers.ModelSerializer):

    transaction_count = serializers.IntegerField(source='transactions.count', read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'type', 'transaction_count']

class TransactionSerializer(serializers.ModelSerializer):

    def validate(self, data):
        transaction_type = data.get('type')
        category = data.get('category')

        if category and category.type != transaction_type:
            raise serializers.ValidationError({
                'category' f" Cannot use category of type '{category.get_type_display()}' for a transaction of type '{transaction_type}'."
            })
        return data



    type_display = serializers.CharField(source='get_type_display', read_only=True)

    category = CategorySerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'type', 'type_display', 'date', 'description', 'created_at', 'updated_at', 'category', 'category_id']

        read_only_fields = ['id', 'created_at', 'updated_at']


    
