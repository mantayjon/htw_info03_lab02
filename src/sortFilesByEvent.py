import fileObject


class SortFiles:

    def __init__(self, file):
        self.file = file

    def sortBydataType(self):
        jpeg = []
        raw = []

        for singleFile in self.file:
            fileName = singleFile.fileName

            splittedName = fileName.split(".")
            if splittedName[1] == 'jpeg' or splittedName[1] == 'jpg':
                jpeg.append(singleFile)
            else:
                raw.append(singleFile)
        return jpeg, raw
