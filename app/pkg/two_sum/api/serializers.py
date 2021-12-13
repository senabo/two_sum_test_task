from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from app.pkg.two_sum.models import TwoSum
from app.pkg.two_sum.utils import get_two_sum_indexes


class TwoSumSerializer(serializers.ModelSerializer):

    class Meta:
        model = TwoSum
        fields = '__all__'


class CreateTwoSumSerializer(serializers.ModelSerializer):
    """
    Serializer creates TwoSum object and returns only result
    """
    numbers_array = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    target = serializers.IntegerField(write_only=True)
    result = serializers.ListField(read_only=True)

    default_error_messages = {
        'invalid_values': _('Invalid the target value or numbers_array.')
    }

    class Meta:
        model = TwoSum
        fields = ('numbers_array', 'target', 'result')

    def validate(self, attrs):
        target = attrs.get('target')
        nums = attrs.get('numbers_array')
        result = get_two_sum_indexes(nums, target)

        if not result:
            self.fail('invalid_values')

        attrs['result'] = result

        return attrs
