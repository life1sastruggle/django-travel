from rest_framework import serializers

from file.models import AttractionImage


class AttractionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionImage
        fields = "__all__"
