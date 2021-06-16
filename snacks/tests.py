from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack

# Create your tests here.

class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Yahya",
             email="yahya@test.com", 
             password="test123"
        )

        self.snack = Snack.objects.create(
            name="Asac", purchaser=self.user, description="Student" 
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Asac")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.name}", "Asac")
        self.assertEqual(f"{self.snack.purchaser}", "yahya@test.com")
        self.assertEqual(self.snack.description,"Student")


    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Asac")
        self.assertTemplateUsed(response, "snacks/snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_details", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: yahya@test.com")
        self.assertTemplateUsed(response, "snacks/snack_details.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "name": "Student",
                "purchaser": self.user.id,
                "description": "Asac",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_details", args="2"))
        self.assertContains(response, "Student")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"name": "Updated name","purchaser":self.user.id,"description":"New description"}
        )

        self.assertRedirects(response, reverse("snack_details", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)