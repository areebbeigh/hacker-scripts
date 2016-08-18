# Python imports
import os

# Local imports
from src.initialize import Initialize


def generate_config_string():
    """ Generates a configuration string with mock values and  returns it """

    initializer = Initialize()
    test_directory = os.path.join(initializer.BASE_DIRECTORY, "tests", "test_directory")
    test_locations = {
        'ext_dir_1': os.path.join(test_directory, "hs_manage", "extn_dir_1"),
        'ext_dir_2': os.path.join(test_directory, "hs_manage", "extn_dir_2"),
        'music_dir_1': os.path.join(test_directory, "hs_music"),
        'wallpaper_dir_1': os.path.join(test_directory, "hs_wallpaper"),
    }

    test_config = """[hs-backup]
    purge            = 1
    retries          = 10
    backup_location  = D:/
    directory1       = C:/Sample_Dir1
    directory2       = C:/Sample_Dir2

    [hs-browse]
    url1 = www.sampleweb1.com
    url2 = www.sampleweb2.com

    [hs-manage]
    extension_set_1  = .txt, .pptx
    location_1       = %(ext_dir_1)s
    extension_set_2  = .jpg, .png
    location_2       = %(ext_dir_2)s

    [hs-music]
    directory1 = %(music_dir_1)s

    [hs-start]
    program1 = C:/Sample_Dir1/Sample_Prog1.exe

    [hs-wallpaper]
    directory1 = %(wallpaper_dir_1)s

    [hs-work]
    editor   = C:/Sample_Editor1.exe
    project1 = C:/Sample_Dir1
    """ % test_locations
    return test_config
