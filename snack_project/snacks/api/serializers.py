from rest_framework import serializers
from snacks.models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','description','purshaser','timestamp','updated')
        model = Snack


