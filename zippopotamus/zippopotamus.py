import urllib2, json

class Zippopotamus:
	def handleAPIError(self):
		return False

	def unicodeToUTF8(self, input):
	    if isinstance(input, dict):
	        return {self.unicodeToUTF8(key): self.unicodeToUTF8(value) for key, value in input.iteritems()}
	    elif isinstance(input, list):
	        return [self.unicodeToUTF8(element) for element in input]
	    elif isinstance(input, unicode):
	        return input.encode('utf-8')
	    else:
	        return input

	def places(self, zipcode):
		apiUrl = 'http://api.zippopotam.us/us/'
		requestUrl = apiUrl + zipcode
		try:
			response = urllib2.urlopen(requestUrl)
			result = json.load(response)
			return self.unicodeToUTF8(result['places'][0])
		except urllib2.URLError, e:
			print 'Request Failed for ' + zipcode
			return False

	def state(self, zipcode):
		places = self.places(zipcode)
		return {'name': places['state'], 'abbreviation' : places['state abbreviation']}

	def coordinates(self, zipcode):
		places = self.places(zipcode)
		return {'lat': places['latitude'], 'long': places['longitude']}