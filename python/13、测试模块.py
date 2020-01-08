

# 单元测试

import unittest


class Student(object):

    def __init__(self, name, score):

        self.name = name
        self.score = score

    def get_grade(self):

        if self.score < 0 or self.score > 100:
            raise ValueError
        elif self.score >= 80:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

    def test_dic(self):
        self.assertRaises(ZeroDivisionError,test,3,0)
        self.assertRaises(ZeroDivisionError,test,a=3,b=0)
        self.assertRaises(ZeroDivisionError, lambda: 3/0)
        with self.assertRaises(ZeroDivisionError):
            value = 3/0


def test(a,b):
    return a/b

if __name__ == '__main__':

    unittest.main()
