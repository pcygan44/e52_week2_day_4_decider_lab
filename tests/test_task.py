import unittest
from src.task import Task
from src.decider import preferences

class TestTask(unittest.TestCase):
    def setUp(self):
        self.clean = Task("Clean Windows", 30)
        self.wash = Task("Wash Dishes",40)
        self.cook = Task("Cook Dinner", 15)
        self.ironing = Task("Do Ironing", 45)
        self.clothes = Task("Wash Clothes", 70)

    def test_name(self):
        self.assertEqual("Clean Windows", self.clean.description)

    def test_time(self):
        self.assertEqual(40, self.wash.duration)

    def test_preferences_house(self):
        # self.clean = Task("Clean Windows", 30)
        # task1 = Task("Wash the Dishes",40)
        # task2 = Task("Cook Dinner", 15)
        # Task.preferences(self.cook, self.wash)
        self.assertEqual("Wash Dishes",preferences(self.wash, self.cook)) 
        self.assertEqual("Cook Dinner",preferences(self.cook, self.clean)) 
        self.assertEqual("Clean Windows", preferences(self.clean, self.wash))
        self.assertEqual("Wash Dishes", preferences(self.wash, self.clothes))
        self.assertEqual("Cook Dinner", preferences(self.cook, self.ironing))
        self.assertEqual("Clean Windows",preferences(self.clean, self.ironing)) 
        self.assertEqual("Do Ironing",preferences(self.ironing, self.wash)) 
        self.assertEqual("Do Ironing" , preferences(self.ironing, self.wash))
        self.assertEqual("Wash Clothes", preferences(self.clothes, self.cook))
        self.assertEqual("Wash Clothes", preferences(self.clothes, self.clean))
    