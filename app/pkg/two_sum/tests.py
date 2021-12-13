from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from app.pkg.two_sum.models import TwoSum


class TwoSumTestCase(APITestCase):
    two_sum_list_url = reverse('two_sum-list')

    def setUp(self) -> None:
        self.num_array = [1,2,3,5,8]

        self.valid_data = {
            'numbers_array': self.num_array,
            'target': 7
        }
        self.invalid_data = {
            'numbers_array': self.num_array,
            'target': 50
        }

        TwoSum.objects.create(
            numbers_array=self.num_array,
            target=7
        )

    def test_get_two_sum_list_200(self):
        response = self.client.get(self.two_sum_list_url)
        body = response.json()
        self.assertTrue(body.get('count') > 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.json())

    def test_post_two_sum_with_valid_data_201(self):
        response = self.client.post(
            self.two_sum_list_url, data=self.valid_data, format='json'
        )
        body = response.json()
        self.assertEqual(body.get('result'), [1, 3], response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

    def test_post_two_sum_with_invalid_data_400(self):
        response = self.client.post(
            self.two_sum_list_url, data=self.invalid_data, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.json())
