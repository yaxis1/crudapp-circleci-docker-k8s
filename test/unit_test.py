import unittest
import requests


class myunitest(unittest.TestCase):
    api_url = 'http://127.0.0.1/'

    get_url = api_url + 'users' #500
    upd_url = api_url + 'users/<id>' #200
    pos_url = api_url + 'users' #200
    del_url = api_url + 'users/<id>' #200

    def ap_url(self):
        return self.api_url

    def test_get(self):
        r = requests.get(myunitest.get_url)
        self.assertEqual(r.status_code, 500)

    def test_update(self):
        r = requests.get(myunitest.upd_url) 
        self.assertEqual(r.status_code, 405) 

    def test_create(self):
        r = requests.get(myunitest.pos_url)
        self.assertEqual(r.status_code, 500) 

    def test_delete(self):
        r = requests.get(myunitest.del_url)
        self.assertEqual(r.status_code, 405) 


if __name__ == '__main__':
    unittest.main() 

