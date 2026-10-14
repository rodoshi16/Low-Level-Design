class HTTP:
    def __init__(self, builder):
        self.url = url 
        self.method = builder.method()

    class Builder:
        def __init__(self, url):
            self.url = url 
            self._method = "GET"
            self._headers = {}
            self._body = None
            self._timeout = 3000
        
        def method(self, method):
            self._method = method

        def headers(self, headers):
            self._headers = headers
        
        def body(self, body):
            self._body = body
        
        def build(self):
            return HTTP(self)
        
        