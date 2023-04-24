import unittest
from sortFilesByEvent import SortFiles
from fileObject import File


class TestSortFiles(unittest.TestCase):

    def setUp(self):
        self.file01 = File('file1.jpeg', 1)
        self.file02 = File('file2.jpg', 4)
        self.file03 = File('file3.raw', 7)
        self.file04 = File('file4.cr2', 2)
        self.file05 = File('file5.arw', 9)

        self.files = [self.file01, self.file02, self.file03, self.file04, self.file05]

    def test_sortByTimeStamp(self):
        sorter = SortFiles(self.files)
        jpeg, raw = sorter.sortByDataType()

        self.assertEqual(len(jpeg), 2)
        self.assertEqual(len(raw), 3)
        self.assertIn(self.file01, jpeg)
        self.assertIn(self.file02, jpeg)
        self.assertIn(self.file03, raw)


if '__name__' == '__main__':
    unittest.main()
