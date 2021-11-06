from rest_framework import serializers
from .models import ReDicKoatuuRegion, ReDistrict, RegionCenter


class ReDicKoatuuRegionSerializer(serializers.ModelSerializer):
    """
    Сериалайзер для области
    """

    class Meta:
        model = ReDicKoatuuRegion
        fields = [
            "this_id", "name",
        ]


class DistrictSerializer(serializers.ModelSerializer):
    """
    Районы конкретной области
    """
    region = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = ReDistrict
        fields = [
            "name", "region", "this_id", "level"
        ]


class RegionCenterSerializer(serializers.ModelSerializer):
    """
    Города конкретного района
    """
    district = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = RegionCenter
        fields = [
            "name", "district", "this_id", "level"
        ]
