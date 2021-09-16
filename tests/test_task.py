import unittest
from src.task import Task
from src.decider import preferences

class TestTask(unittest.TestCase):
    def setUp(self):
        self.clean = Task("Clean Windows", 30)
        self.wash = Task("Wash the Dishes",40)
        self.cook = Task("Cook Dinner", 15)

    def test_name(self):
        self.assertEqual("Clean Windows", self.clean.description)

    def test_time(self):
        self.assertEqual(40, self.wash.duration)

    def test_preferences_house(self):
        # self.clean = Task("Clean Windows", 30)
        # task1 = Task("Wash the Dishes",40)
        # task2 = Task("Cook Dinner", 15)
        # Task.preferences(self.cook, self.wash)
        self.assertEqual("Wash the Dishes",preferences(self.wash, self.cook)) 