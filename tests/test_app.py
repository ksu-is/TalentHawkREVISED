import unittest
from talenthawk.app import app

class TalentHawkTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test that the home page loads correctly
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Soccer Player Analytics', response.data)

    def test_player_detail(self):
        # Test that a player detail page loads correctly
        response = self.app.get('/player/player1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Lionel Messi', response.data)

    def test_comparison_page(self):
        # Test that the comparison page loads correctly
        response = self.app.get('/comparison')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Player Comparison Tool', response.data)

    def test_analytics_page(self):
        # Test that the analytics page loads correctly
        response = self.app.get('/analytics')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Advanced Player Analytics', response.data)

if __name__ == '__main__':
    unittest.main() 