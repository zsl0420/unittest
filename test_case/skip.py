import unittest
class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试用例")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(3 > 2,"当条件为真时跳过测试用例")
    def test_skip_if(self):
        print('test_bbb')

    @unittest.skipUnless(3 > 2,"当测试条件为真时执行测试")
    def test_skip_unless(self):
        print('test_ccc')

    @unittest.expectedFailure
    def test_expected_Failure(self):
        self.assertEqual(2, 3)

if __name__ == '__main__':
    unittest.main()
