class Playlist(file):
    '''Simple PLS file helper'''

    def __init__(self,filename):
        file.__init__(self,filename)
        self.closet = True
        data = self.__getLines('title','file','version','numberofentries')
        self.titles = data['title']
        self.files = data['file']
        self.version = data['version'][0]
        self.entriescount = data['numberofentries'][0]

    def __getLines(self,*patterns):
        result = {}
        for patt in patterns:
            result[patt] = []

        for line in self:
            for patt in patterns:
                if line.lower().startswith(patt):
                    result[patt].append(line.strip().split('=')[-1])

        return result

    def getTitles(self):
        'Returns a list of all titles ina .pls file'
        return self.titles

    def getFiles(self):
        'Returns a list of all files/streams in a .pls file'
        return self.files

    def getVersion(self):
        'Returns version found in a .pls file'
        return self.version

    def getEntriesCount(self):
        'Returns number of entries in a .pls file'
        return self.entriescount

    def getFileByTitle(self,title):
        'Returns file/stream name for a given title'
        return self.files[ self.titles.index(title) ]

    def getTitleByFile(self,filename):
        'Returns title for a given file/stream name'
        return self.titles[ self.files.index(filename) ]

    def getTitlesAndFiles(self):
        'Returns a list of titles and files in .pls file'
        return zip(self.titles,self.files)
