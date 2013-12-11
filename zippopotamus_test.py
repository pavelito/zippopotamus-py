from zippopotamus import Zippopotamus
import unittest

class TestZippopotamusPy(unittest.TestCase):

	def setUp(self):
		self.zipcode = '10010'
		self.zipcodeWrong = '100100'
		self.zippo = Zippopotamus('us')
		self.zippoResults = {}
		self.zippoResults['coordinates'] = {'lat': '40.7375', 'long': '-73.9813'}
		self.zippoResults['state'] = {'abbreviation': 'NY', 'name': 'New York'}
		self.zippoResults['places'] = [{'latitude': '40.7375', 'state': 'New York', 'state abbreviation': 'NY', 'place name': 'New York City', 'longitude': '-73.9813'}]

	def test_coordinates(self):
		self.assertEqual(self.zippo.coordinates(self.zipcode), self.zippoResults['coordinates'])

	def test_state(self):
		self.assertEqual(self.zippo.state(self.zipcode), self.zippoResults['state'])

	def test_places(self):
		self.assertEqual(self.zippo.places(self.zipcode), self.zippoResults['places'])

	def test_wrong_coordinates(self):
		self.assertEqual(self.zippo.coordinates(self.zipcodeWrong), {})

	def test_wrong_state(self):
		self.assertEqual(self.zippo.state(self.zipcodeWrong), {})

	def test_wrong_places(self):
		self.assertEqual(self.zippo.places(self.zipcodeWrong), [])


if __name__ == '__main__':
	unittest.main()
	'''		
	zippo = Zippopotamus('us')
	print zippo.places('10010')
	'''
