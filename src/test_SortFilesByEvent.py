import unittest
from sortFilesByEvent import SortFiles
import main
from fileObject import File

jpgTest = ['DSC03767.jpeg', 'DSC03766.jpg']
rawTest = ['DSC03965.ARW']


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass


    '''
    def test_folderPath(self):
        print()
        folderPath = ["Lab02/Pictures"]
        self.assertTrue(folderPath == "Lab02/Pictures")


    def test_sortByDataType(self):
        arrJpg = SortFiles.sortByDataType(self)
        arrRaw = SortFiles.sortByDataType(self)

        self.assertTrue(arrJpg == jpgTest)
        self.assertTrue(arrRaw == rawTest)
'''


if __name__ == '__main__':
    unittest.main()
