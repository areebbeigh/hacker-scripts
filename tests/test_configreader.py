# Python imports
import configparser
import os
import unittest

# Local imports
from src import configreader
from src.initialize import Initialize
from tests.configgenertor import generate_config_string

initializer = Initialize()
test_directory = os.path.join(initializer.BASE_DIRECTORY, "tests", "test_directory")
test_config = generate_config_string()


class ConfigReaderTestCase(unittest.TestCase):
    """
    These tests are written for the individual read methods in the
    configreader.ConfigReader() module. A mock configuration and
    directory tree (tests/test_directory) is used for testing.
    """

    def setUp(self):
        self.reader = configreader.ConfigReader("")
        self.Config = configparser.ConfigParser()
        self.Config.read_string(test_config)

    def test_read_backup(self):
        purge, retries, backup_loc, directories = self.reader._read_backup(self.Config)
        self.assertEqual(purge, '1')
        self.assertEqual(retries, '10')
        self.assertEqual(backup_loc, "D:/")
        self.assertEqual(directories, ["C:/Sample_Dir1", "C:/Sample_Dir2"])

    def test_read_browse(self):
        urls = self.reader._read_browse(self.Config)
        self.assertEqual(urls, ["www.sampleweb1.com", "www.sampleweb2.com"])

    def test_read_manage(self):
        result = self.reader._read_manage(self.Config)
        expected_result = {
            ('.txt', '.pptx'): os.path.join(test_directory, "hs_manage", "extn_dir_1"),
            ('.jpg', '.png'): os.path.join(test_directory, "hs_manage", "extn_dir_2"),
        }
        self.assertEqual(result, expected_result)

    def test_read_music(self):
        result = self.reader._read_music(self.Config)
        expected_result = [
            os.path.join(test_directory, "hs_music", "fake_music1.mp3"),
            os.path.join(test_directory, "hs_music", "fake_music2.mp3"),
            os.path.join(test_directory, "hs_music", "more music", "fake_music3.mp3"),
        ]
        self.assertEqual(result, expected_result)

    def test_read_start(self):
        result = self.reader._read_start(self.Config)
        self.assertEqual(result, ["C:/Sample_Dir1/Sample_Prog1.exe"])

    def test_read_wallpaper(self):
        result = self.reader._read_wallpaper(self.Config)
        expected_result = [
            os.path.join(test_directory, "hs_wallpaper", "fake_wallpaper1.jpg"),
            os.path.join(test_directory, "hs_wallpaper", "fake_wallpaper2.jpg"),
            os.path.join(test_directory, "hs_wallpaper", "more wallpapers", "fake_wallpaper3.jpg"),
        ]
        self.assertEqual(result, expected_result)

    def test_read_work(self):
        files, editor = self.reader._read_work(self.Config)
        self.assertEqual(files, ["C:/Sample_Dir1"])
        self.assertEqual(editor, "C:/Sample_Editor1.exe")


if __name__ == '__main__':
    unittest.main()
