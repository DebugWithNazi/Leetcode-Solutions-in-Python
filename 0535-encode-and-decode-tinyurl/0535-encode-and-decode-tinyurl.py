class Codec:
    def __init__(self):
        self.encodeDict = {}
        self.decodeDict = {}
        self.base = "http://tinyurl.com/"        

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.encodeDict:
            shortUrl = self.base + str(len(self.encodeDict) + 1)
            self.encodeDict[longUrl] = shortUrl
            self.decodeDict[shortUrl] = longUrl
        return self.encodeDict[longUrl]      

    def decode(self, shortUrl: str) -> str:
        return self.decodeDict[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))