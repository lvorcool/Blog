from django.test import TestCase
from studyone.models import users
# Create your tests here.
class ModelTest(TestCase):

    def setUp(self):
        users.objects.create(id=1, usersname="liu", password="123456", name="liudaha", sex=1, createOn="2017-11-01 23:10:11")

    def test_users_models(self):
        result = users.objects.get(usersname="liu")
        self.assertEqual(result.name, "liudaha")
