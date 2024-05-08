from rest_framework import generics
from api.models import NamesWoman
from api.serializers import NamesWomanSerializer


class CreateNamesWomanView(generics.CreateAPIView):
    """Добавление женсого имени"""

    serializer_class = NamesWomanSerializer


class DeleteNamesWomanByIdView(generics.DestroyAPIView):
    """Удаление женсого имени по идентификации"""

    queryset = NamesWoman.objects.all()


class GetNamesWomanView(generics.ListAPIView):
    """Вывод женских имён"""

    queryset = NamesWoman.objects.all()
    serializer_class = NamesWomanSerializer
