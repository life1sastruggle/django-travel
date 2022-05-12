from rest_framework import serializers

from attraction.models import Attraction
from file.serializers import AttractionImageSerializer


class AttractionSerializer(serializers.ModelSerializer):
    attraction_image = AttractionImageSerializer(many=True)

    class Meta:
        model = Attraction
        fields = "__all__"
