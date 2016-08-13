# Python imports
import unittest
import configparser

# Local imports
from src import configreader
from src.errors import ConfigError


class ConfigReaderTestCase(unittest.TestCase):
    """
    These tests use the "test_config.ini" file as input to the
    configreader.ConfigReader() class methods and tests whether the return
    values are the same as in the mock configuration file
    """

    def setUp(self):
        self.reader = configreader.ConfigReader("tests/test_config.ini")

    def test_read_backup(self):
        purge, retries, backup_loc, directories = self.reader.read_config("hs-backup")
        self.assertEqual(purge, '1')
        self.assertEqual(retries, '10')
        self.assertEqual(backup_loc, "D:/")
        self.assertEqual(directories, ["C:/Sample_Dir1", "C:/Sample_Dir2"])

    def test_read_browse(self):
        urls = self.reader.read_config("hs-browse")
        self.assertEqual(urls, ["www.sampleweb1.com", "www.sampleweb2.com"])

    def test_read_manage(self):
        with self.assertRaises(ConfigError):
            self.reader.read_config("hs-manage")

    def test_read_music(self):
        result = self.reader.read_config("hs-music")
        self.assertEqual(result, [])

    def test_read_start(self):
        result = self.reader.read_config("hs-start")
        self.assertEqual(result, ["C:/Sample_Dir1/Sample_Prog1.exe"])

    def test_read_wallpaper(self):
        result = self.reader.read_config("hs-wallpaper")
        self.assertEqual(result, [])

    def test_read_work(self):
        files, editor = self.reader.read_config("hs-work")
        self.assertEqual(files, ["C:/Sample_Dir1"])
        self.assertEqual(editor, "C:/Sample_Editor1.exe")

if __name__ == '__main__':
    unittest.main()
