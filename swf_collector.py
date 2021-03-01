import requests
import validators

def urlprocess (url):
    if url [:2] == "//":
        url = "https:" + url
    return url

class SWF:
    def __init__ (self):
        self.req = requests.session ()

    def getPage (self, url):
        self.response = self.req.get (url)
        self.content = self.response.content.decode (encoding = "latin-1")

    def get (self, divisors = '"'):
        self.format = self.content.find (".swf")
        if self.format == -1:
            return -1
        else:
            self.end = self.format
            self.start = self.format

            while not self.content [self.end] == divisors:
                self.end += 1

            while not self.content [self.start - 1] == divisors:
                self.start -= 1

            self.swfUrl = urlprocess (self.content [self.start : self.end])
            if validators.url (self.swfUrl) == True:
                return self.swfUrl
            else:
                return "non valid"

    def getNext (self, divisors = '"'):
        self.content = self.content [: self.format] + "a" + self.content [self.format + 1 :]
        return self.get (divisors = divisors)

    def download (self, path):
        file = open (path, "wb")
        print ("File created")
        print (self.swfUrl)
        file.write (self.req.get (self.swfUrl).content)