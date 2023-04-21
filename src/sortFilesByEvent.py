import fileObject


class SortFiles:

    def __init__(self, *file):
        self.file = file

    def sortBydataType(self):
        jpeg = []
        raw = []

        for singleFile in self.file:
            print(singleFile)
            print(singleFile)
            """fileName = singleFile.split(".")
            if fileName[1] == 'jpeg' or fileName[1] == 'jpg':
                jpeg.append(singleFile)
            else:
                raw.append(singleFile)
"""