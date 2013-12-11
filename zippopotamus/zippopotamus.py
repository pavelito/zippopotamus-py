import urllib2, json

class Zippopotamus:

	def __init__(self, countryCode = 'us'):
		self.countryCode = countryCode.lower()
		self.cache = {}

	def handleAPIError(self):
		pass

	def unicodeToUTF8(self, input):
	    if isinstance(input, dict):
	        return {self.unicodeToUTF8(key): self.unicodeToUTF8(value) for key, value in input.iteritems()}
	    elif isinstance(input, list):
	        return [self.unicodeToUTF8(element) for element in input]
	    elif isinstance(input, unicode):
	        return input.encode('utf-8')
	    else:
	        return input

	def getAPIResult(self, zipcode):
		apiUrl = 'http://api.zippopotam.us/'
		requestUrl = apiUrl + self.countryCode + '/' + urllib2.quote(zipcode)
		try:
			response = urllib2.urlopen(requestUrl)
			result = json.load(response)
			self.cache[zipcode] = self.unicodeToUTF8(result)
			return self.cache[zipcode]
		except urllib2.URLError, e:
			#print 'Request Failed for ' + zipcode
			return False

	def __getResult(self, zipcode):
		if zipcode in self.cache:
			return self.cache[zipcode]
		else:
			return self.getAPIResult(zipcode)

	def places(self, zipcode):
		result = self.__getResult(zipcode)
		if result == False:
			return []
		else:
			return result['places']

	def state(self, zipcode):
		places = self.places(zipcode)
		if not places:
			return {}
		return {'name': places[0]['state'], 'abbreviation' : places[0]['state abbreviation']}

	def coordinates(self, zipcode):
		places = self.places(zipcode)
		if not places:
			return {}
		return {'lat': places[0]['latitude'], 'long': places[0]['longitude']}