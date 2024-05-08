from rest_framework import generics
from api.models import NamesMan
from api.serializers import NamesManSerializer


class CreateNamesManView(generics.CreateAPIView):
    """Добавление мужского имени"""

    serializer_class = NamesManSerializer


class DeleteNamesManByIdView(generics.DestroyAPIView):
    """Удаление мужского имени по идентификации"""

    queryset = NamesMan.objects.all()


class GetNamesManView(generics.ListAPIView):
    """Вывод мужских имён"""

    queryset = NamesMan.objects.all()
    serializer_class = NamesManSerializer
