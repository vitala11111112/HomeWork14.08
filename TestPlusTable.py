import PlusTable
import unittest
import random
class TestPlusTable(unittest.TestCase):
    def setUp(self):
        self.obj = PlusTable.PlusTable()
    def test_read(self):
        for i in range(1000):
            summand1 = random.randint(-100,100)
            summand2 = random.randint(-100,100)
            result =  summand1 +  summand2
            self.obj.insert(summand1,summand2,result)
            self.assertEqual(( summand1, summand2,result),self.obj.read())
unittest.main()
