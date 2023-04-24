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

    def test_sortByFileName(self):
        sorter = SortFiles(self.files)
        jpeg, raw = sorter.sortByDataType()

        expJpeg = [self.file01, self.file02]
        expRaw = [self.file03, self.file04, self.file05]

        self.assertEqual(len(jpeg), 2)
        self.assertEqual(jpeg, expJpeg)
        self.assertIn(self.file01, jpeg)
        self.assertIn(self.file02, jpeg)

        self.assertEqual(len(raw), 3)
        self.assertEqual(raw, expRaw)
        self.assertIn(self.file03, raw)
        self.assertIn(self.file04, raw)
        self.assertIn(self.file05, raw)

    def test_sortByTimeStamp(self):
        sorter = SortFiles(self.files)
        sorted_Timestamp = sorter.sortByTimeStamp()

        expStamp = [self.file01, self.file04, self.file02, self.file03, self.file05]

        self.assertEqual(sorted_Timestamp, expStamp)


if '__name__' == '__main__':
    unittest.main()
