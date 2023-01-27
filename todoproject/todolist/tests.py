from django.test import TestCase
from todolist.models import Task, TaskList

# Create your tests here.
class TaskTest(TestCase):
	"""Test sur les tâches"""
	def test_str(self):
            task1 = Task.objects.create(title="Ma tâche", done=True)
            self.assertEquals(task1.__str__(), "Ma tâche")
    
class TestTodoList(TestCase):
    def setUp(self):
        self.task1 = Task.objects.create(title="Ma tâche", done=True)    
        
    def test_resolve_home_url(self):
        response = self.client.get('/todo/tasks/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ma tâche")

    # tester que le formulaire réussisse bien à inscrire une tâche en BDD
    def test_task_add(self):
        response = self.client.post('/todo/add_task/', 
        data={
            'title':'Faire le test',
            'deadline':'2023-01-27',
            'done':False
            }
        )
        task2 = Task.objects.filter(title="Faire le test")
        self.assertEqual(task2.count(), 1)
