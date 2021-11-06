from .serializers import (
    ReDicKoatuuRegionSerializer,
    DistrictSerializer,
    RegionCenterSerializer
)
from .models import (
    ReDicKoatuuRegion,
    ReDistrict,
    RegionCenter
)
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.


class ListReDicKoatuuRegionAPI(APIView):
    """
    Вывод списка областей полный
    """

    def get(self, request):
        regions = ReDicKoatuuRegion.objects.all().order_by("name")
        serializers = ReDicKoatuuRegionSerializer(regions, many=True)
        return Response(serializers.data)


class DistrictsAPI(APIView):
    """
    Районы
    """

    def get(self, request, pk):
        regions = ReDicKoatuuRegion.objects.get(this_id=pk)
        districts = ReDistrict.objects.filter(region=regions).order_by("name")
        serializers = DistrictSerializer(districts, many=True)
        return Response(serializers.data)


class RegionCenterAPI(APIView):
    """
    Города от районов
    """

    def get(self, request, pk):
        districts = ReDistrict.objects.get(this_id=pk)
        cities = RegionCenter.objects.filter(district=districts).order_by("name")
        serializers = RegionCenterSerializer(cities, many=True)
        return Response(serializers.data)
