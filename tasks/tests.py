from django.test import TestCase, Client
from .models import Task, Categories
from django.urls import reverse
from datetime import date

# Create your tests here.

class TaskAppTests(TestCase):
    def setUp(self):
        self.categories = Categories.objects.create(name="テストカテゴリ")
        self.task = Task.objects.create(
            title="テストタスク",
            description="説明",
            start_date=date.today(),
            until_date=date.today(),
            categories=self.categories
        )
        self.client = Client()

    def test_task_list_view(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "テストタスク")

    def test_add_task_api(self):
        data = {
            "title": "APIタスク",
            "description": "API説明",
            "start_date": "2024-07-01",
            "until_date": "2024-07-02",
            "category_id": self.categories.id
        }
        response = self.client.post(
            reverse('add_task_api'),
            data=data,
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Task.objects.filter(title="APIタスク").exists())

    def test_delete_task_api(self):
        response = self.client.post(reverse('delete_task_api', args=[self.task.id]))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())

    def test_add_categories_api(self):
        response = self.client.post(
            reverse('add_categories_api'),
            data={"name": "新カテゴリ"},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Categories.objects.filter(name="新カテゴリ").exists())
