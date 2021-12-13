from rest_framework import viewsets

from app.pkg.two_sum.api.serializers import TwoSumSerializer, CreateTwoSumSerializer
from app.pkg.two_sum.models import TwoSum


class TwoSumView(viewsets.ModelViewSet):
    serializer_class = TwoSumSerializer
    queryset = TwoSum.objects.all()
    http_method_names = ['get', 'post', 'delete']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateTwoSumSerializer
        return super(TwoSumView, self).get_serializer_class()
