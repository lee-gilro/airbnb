from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Perk
from .serializers import PerkSerializer
# Create your views here.
class Perks(APIView):
    
    def get(self, request):
        all_perks = Perk.objects.all()
        serializer = PerkSerializer(all_perks, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerkSerializer(data=request.data)
        if serializer.is_valid():
            user_input = serializer.save()
            return Response(PerkSerializer(user_input).data)
        else:
            return Response(serializer.errors)



class PerkDetail(APIView):
    def get_object(self, pk):
        try:
            return Perk.objects.get(pk=pk)
        except Perk.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        perk = self.get_object(pk=pk)
        serializer = PerkSerializer(perk)
        return Response(serializer.data)

    def put(self, request, pk):
        perk = self.get_object(pk=pk)
        serializer = PerkSerializer(perk, data=request.data, partial = True)
        if serializer.is_valid():
            update_perk = serializer.save()
            return Response(PerkSerializer(update_perk).data)
        else:
            return Response(serializer.errors)

    def delete(self, request , pk):
        perk = self.get_object(pk=pk)
        perk.delete()
        return Response(status = HTTP_204_NO_CONTENT)