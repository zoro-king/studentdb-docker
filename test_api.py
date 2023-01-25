import unittest
import requests

class TestApi(unittest.TestCase):
    url="http://localhost:5000/"
    data={
        "name":"yuva",
        "department":"MCA",
        "year":"II"
    }

    def test_home(self):
        response = requests.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()), 5)
        print("Test 1 passed")

    def test_post_stddb(self):
        response=requests.post(self.url ,json = self.data)
        self.assertEqual(response.status_code,200)
        print("Test 2 passed")


if __name__ == "__main__":
    tester=TestApi()
    tester.test_home()
    #tester.test_post_stddb()