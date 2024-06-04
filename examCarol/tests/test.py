import unittest
from app import app
from flask import session


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_redirect(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.headers['Location'])
        print("Lanzamiento de la redireccion de login")

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)
        print("test login")

    def test_login_failure(self):
        response = self.app.post(
            '/login', data=dict(username='admin', password='wrongpassword'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Datos incorrectos, intentelo de nuevo', response.data)
        print('test de fallo de inicio de sesion')

    def test_logout(self):
        self.app.post('/login', data=dict(username='admin',
                      password='password'), follow_redirects=True)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)
        print("test de logout")


if __name__ == '__main__':
    unittest.main()