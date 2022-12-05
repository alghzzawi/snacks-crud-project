from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.
class SnackTest(TestCase):
    def test_list_view_status(self):
        url=reverse('snack_list')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_create_view_status(self):
        url=reverse('snack_create')
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def setUp(self):
        self.user=get_user_model().objects.create_user( # create supper user
            username='test',
            email='test@test.com',
            password='test'
        )
        self.scack=Snack.objects.create(
            title='test',
            purchaser=self.user,
            description='that for test'
        )

    def test_detail_view(self):
        url=reverse('snack_detail',args=[self.scack.id])
        response=self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')

    def test_create_view(self):
        data={
            'title':'test',
            'purchaser':self.user.id,
            'description':'that for test'
        }

        url=reverse('snack_create')
        response=self.client.post(path=url,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertRedirects(response,reverse('snack_detail',args=[2]))