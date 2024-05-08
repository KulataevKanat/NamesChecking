from rest_framework.response import Response
from rest_framework import generics, status
import requests

from api.models import NamesMan, NamesWoman
from api.serializers import ContactSerializer
from api.service import get_gender_value
from names_checking.bitrix_data import webhook_url, gender_uf_name, contact_id, contact_name, gender_male_id, gender_female_id


class UpdateContacts(generics.ListAPIView):
    """Обновление данных по гендеру обратно в контакт по ID"""

    def get(self, request, *args, **kwargs):
        contact_list = f"{webhook_url}/crm.contact.list"
        params = {'select[]': [contact_id, contact_name, gender_uf_name]}
        list_response = requests.get(contact_list, params=params)

        contacts_list = list_response.json()

        for contact in contacts_list["result"]:

            # Проверка имён контактов на наличие их в БД (PostgreSQL):
            is_male = NamesMan.objects.filter(name=contact[contact_name]).exists()
            is_female = NamesWoman.objects.filter(name=contact[contact_name]).exists()

            gender = None

            # Если имя найдено в БД мужчин:
            if is_male:
                gender = gender_male_id  # ID мужского пола в пользовательском поле в Bitrix24

            # Если имя найдено в БД женщин:
            elif is_female:
                gender = gender_female_id  # ID женского пола в пользовательском поле Bitrix24

            bitrix_data = {
                'id': contact[contact_id],
                'fields': {
                    gender_uf_name: gender,
                }
            }

            # Обновление данных по гендеру обратно в контакт по ID:
            contact_post = f"{webhook_url}/crm.contact.update"
            requests.post(contact_post, json=bitrix_data)

        return Response({'message': 'Contacts updated successfully'}, status=status.HTTP_200_OK)


class GetContactsView(generics.ListAPIView):
    """Получение данных контакта (ID, Имя, Пол) из Битрикс24 по Webhook"""

    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        contact_list = f"{webhook_url}/crm.contact.list"
        params = {'select[]': [contact_id, contact_name, gender_uf_name]}
        list_response = requests.get(contact_list, params=params)

        contacts_list = list_response.json()
        data = list()
        for contact in contacts_list["result"]:
            gender = get_gender_value(contact[gender_uf_name])
            data.append({
                'id': contact[contact_id],
                'name': contact[contact_name],
                'gender': gender
            })
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
