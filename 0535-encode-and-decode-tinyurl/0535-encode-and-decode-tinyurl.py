class Codec:

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.count = 0

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url_to_code:
            self.count += 1
            code = str(self.count)

            self.url_to_code[longUrl] = code
            self.code_to_url[code] = longUrl

        return "http://tinyurl.com/" + self.url_to_code[longUrl]

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.split("/")[-1]
        return self.code_to_url[code]