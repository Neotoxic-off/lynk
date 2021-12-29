import re

class Lynk:
    def __init__(self):
        self.regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        self.links = []

    def feed(self, content):
        self.links = []
        results = re.findall(self.regex, content)

        for result in results:
            for link in result:
                if (self.__check__(link) == True):
                    self.links.append(link)

        return (self.links)

    def __check__(self, link):
        tests = [
            link != None,
            len(link) > 3,
            link not in self.links,
            (link.startswith("https://") or link.startswith("http://"))
        ]

        for test in tests:
            if (test == False):
                return (False)
        return (True)