from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import *

# Create your tests here.
class PerevalAPITestCase(APITestCase):
    def setUp(self):
        self.user = MyUser.objects.create(
            email="qwerty@mail.ru",
            fam="Фамилия",
            name="Имя",
            otc="Отчество",
            phone="+7 555 55 55"
        )
        self.coords = Coords.objects.create(
            latitude="12.3456",
            longitude="5.6789",
            height="2500"
        )
        self.level = Level.objects.create(
            winter="2А",
            spring="2А",
            summer="2А",
            autumn="2А",
        )
        self.pereval = Pereval.objects.create(
            beauty_name="пер.",
            title="Название",
            other_titles="Альтернативное название",
            connect="Соединяет что-то",
            user=self.user,
            coords=self.coords,
            level=self.level
        )
        Images.objects.create(data="<картинка1>", title="Седловина", pereval=self.pereval)
        Images.objects.create(data="<картинка2>", title="Подъем", pereval=self.pereval)

    def submitData_test(self):
        url = reverse('pereval-list')
        data = {
            "beauty_name": "пер.",
            "title": "Новый",
            "other_titles": "перевал",
            "connect": "соединяет",
            "user": {
                "email": "pochta@mail.ru",
                "fam": "Роман",
                "name": "Роман",
                "otc": "Романови",
                "phone": "89995786231"
            },
            "coords": {
                "latitude": "47.3842",
                "longitude": "11.1525",
                "height": "1700"
            },
            "level": {
                "winter": "2А",
                "spring": "1А",
                "summer": "1А",
                "autumn": "2А"
            },
            "status": "NW",
            "images": [{"data":"ссылка1", "title":"Пик"}, {"data":"ссылка2", "title":"Начало"}]
        }

        # проверка, что запрос отправлен
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # проверка, что объект сохранён в бд и не None
        new_pereval = Pereval.objects.filter(beauty_title="пер.", title="Новый")
        self.assertIsNotNone(new_pereval)

        self.assertIn('status', response.data)
        self.assertIn('message', response.data)
        self.assertIn('id', response.data)
        self.assertEqual(response.data['status'], 200)
        self.assertEqual(response.data['message'], "Отправлено успешно")

    def test_missing_filed(self):
        '''Пропускаю одно поле, закоментировав его'''

        url = reverse('pereval-list')
        data = {
            "beauty_name": "пер.",
            "title": "Новый",
            "other_titles": "перевал",
            #"connect": "соединяет",
            "user": {
                "email": "pochta@mail.ru",
                "fam": "Роман",
                "name": "Роман",
                "otc": "Романови",
                "phone": "89995786231"
            },
            "coords": {
                "latitude": "47.3842",
                "longitude": "11.1525",
                "height": "1700"
            },
            "level": {
                "winter": "2А",
                "spring": "1А",
                "summer": "1А",
                "autumn": "2А"
            },
            "status": "NW",
            "images": [{"data": "ссылка1", "title": "Пик"}, {"data": "ссылка2", "title": "Начало"}]
        }
        response = self.client.post(url, data, format='json')
        # проверим, что вернётся сообщение status: 400, message: "Bad Request"
        self.assertIn('status', response.data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['status'], 400)
        self.assertEqual(response.data['message'], "Bad Request")

    def test_retrieve_success(self):
        url = reverse('pereval-detail', kwargs={'pk': self.pereval.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.pereval.id)
        self.assertEqual(response.data['beauty_name'], self.pereval.beauty_name)
        self.assertEqual(response.data['title'], self.pereval.title)

    def test_fail_retrieve(self):
        url = reverse('pereval-detail', kwargs={'pk': self.pereval.pk + 1})
        response = self.client.get(url)
        self.assertIn('state', response.data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['state'], 0)
        self.assertEqual(response.data['message'], "Запись с таким id не найдена")

