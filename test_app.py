import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movie


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the Casting Agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "postgres"
        self.database_path = "postgres://{}/{}".format(
            'postgres:123456@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

            self.Casting_Assistant = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikw5ek5VYWRITldKRkJsWGhTSkpLYiJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzUzYzI4Y2RmYjNjMGM3ZTQzZGEzOCIsImF1ZCI6ImNhcHN0b24iLCJpYXQiOjE1OTA0NDYwODUsImV4cCI6MTU5MDQ1MzI4NSwiYXpwIjoidGo0SUNkNWR3NEVMWllaaUMwc2pRNkh6YlRxZzZxVnciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWUiXX0.rV1jB9pywEOPuwXznQHgirTralV7H06mdL-p9MOSdgjpSCjBU4nhHyzw32KCCTBw9FJexw9CZekBq1ADFyd3tUpuhmpjsZyxnw3a9kb93cvQoJROFGkF3Dpl_IV4SAmLaK-_h1S9DZdUGpVqoahARb1_rmJNFMFt-I6ZlTdgfu69phgcX3Wj_wWspsxdGFf6CDVv0x-8KZa8U-T_t9LZSZrwwPELzh67hVH7I21G5wY0KNTmNaK05S6v8rSSX0yEksgZIP4tDKVzgkiRSTJF8ry5XTkxW2-WHq5ndhiIJrGzKZdYdj9tUX8cVhFGjS7804rTmqng3Q8oDN35rUoSTg')
            self.Casting_Director = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikw5ek5VYWRITldKRkJsWGhTSkpLYiJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzUzYzc1NzIwYWQ3MGM3MmI2ZWE0YyIsImF1ZCI6ImNhcHN0b24iLCJpYXQiOjE1OTA0NDYxNTksImV4cCI6MTU5MDQ1MzM1OSwiYXpwIjoidGo0SUNkNWR3NEVMWllaaUMwc2pRNkh6YlRxZzZxVnciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllIiwidXBkYXRlOmFjdG9yIiwidXBkYXRlOm1vdmllIl19.NTRR5YMxdC86nVOHaJ5q9Pgb2y9pLE1KUllgDDy3QiHGJ7w5UIubE0i5DapnwDRjlmS1wiMutIDSmto3VBlkyVGRQZQykk2X3gGMmRe0o4FiqvAxgYjdUFJ9rErGeyRqPKtIDNjBA8z1M0Fq9XKxoERF136Vq_QH1HOdsPym0Oq9jFcWi-XbX9hWH1xxzx7_ZMyXbrkMJcdoyRwtEGGqe-vj04NIPaTd58cdUVJFB4zMJaw_wz8cz8XV5saiwgJZCEB3Gba051tIJGHvcaKoJqhFD9uSfLKVAqLYB6KcuvVNf2wbrOcvjznnahgWom1tm4UISGixqMhOSTUBYhbPHQ')
            self.Executive_Producer = ('eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ikw5ek5VYWRITldKRkJsWGhTSkpLYiJ9.eyJpc3MiOiJodHRwczovL2NhcHN0b24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzUzY2UyNzIwYWQ3MGM3MmI2ZWM0ZCIsImF1ZCI6ImNhcHN0b24iLCJpYXQiOjE1OTA0NDYyMjQsImV4cCI6MTU5MDQ1MzQyNCwiYXpwIjoidGo0SUNkNWR3NEVMWllaaUMwc2pRNkh6YlRxZzZxVnciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbXX0.t5zVCpSsV-WeUoUUhQUXZG1ZDC0RWwJaKboq3n55gKABDfswpHK1XoCpeM-sXdB2JAETAuvSRwktQi-cu8tRHLP4caC2JobcdH_Ir_OUAlhX2dpHq9_6PmoyX1GEooP0NbZb8Gstav1-zyjMK_a0hBH2OOXd5pdrljiaqUYZJBVIKFBNddtQ2B1N7k2viHSCmiJPfaZb3B26t_y9WcUJAQU5OQSVLXYbUqfvrnsbKzcZH8gXg6DD6E8WY0dCSR3KKv6_lNh28TcONRrmaB00dpp1vuuHvlFo-wn8-JdKCQCQHu1yqMP3gUx85nBxXT9gZzUWneNvuPBAlt2PzivWBw')

        self.new_movie = {
            'title': 'Avengers 2',
            'release_date': '2021-10-1 04:22'
        }
        self.new_actor = {
            'name': 'John Doe',
            'age': 20,
            'gender': 'Male'
        }

        self.update_movie = {
            'title': 'Toy Story 12',
            'release_date': '2021-10-1 04:22'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) >= 0)

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) >= 0)

    def test_create_movies(self):
        res = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "Authorization": (Executive_Producer)})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        # self.assertTrue(len(data['movies']) == 13)

    def test_create_actors(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "Authorization": (Casting_Director)})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        # self.assertTrue(len(data['actors']) == 1)

    def test_update_movies(self):
        # self.client().post('/movies', json=self.new_movie)
        res = self.client().patch('/movies/22', json=self.update_movie,
                                  headers={"Authorization": (Casting_Director)})
        data = json.loads(res.data)

        self.assertTrue(data['success'])
        # self.assertTrue(len(data['movies']) == 22)

    def test_delete_actors(self):
        self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "Authorization": (Casting_Director)})

        res = self.client().delete('/actors/22')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['delete'], '22')
        self.assertTrue(data['success'])

    def test_delete_movies(self):
        self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "Authorization": (Executive_Producer)})
        res = self.client().delete('/movies/32')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['delete'], '32')
        self.assertTrue(data['success'])

    #  ----------------------------------------------------------------
    #  Error behavior tests
    #  ----------------------------------------------------------------

    def test_401_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_create_actors(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_401_create_movies(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_404_update_actors(self):
        res = self.client().patch('/actors/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_update_movies(self):
        res = self.client().patch('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_delete_actors(self):
        res = self.client().delete('/actors/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

    def test_404_delete_movies(self):
        res = self.client().delete('/movies/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
