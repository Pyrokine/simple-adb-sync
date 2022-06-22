import os
import shutil
import subprocess
import datetime
import time

date = str(datetime.datetime.now().strftime('%Y.%m.%d')[2:])


def adb(command):
    proc = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, shell=True)
    [out, _] = proc.communicate()
    print(out)


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except Exception as e:
        pass


def download_files(mobile_prefix, mobile_folder_name, pc_prefix, pc_folder_name):
    print('Downloading from [{}] to [{}]. Please wait...'.format(
        os.path.join(mobile_prefix, mobile_folder_name),
        os.path.join(pc_prefix, pc_folder_name)
    ))

    start_time = time.time()
    create_folder(os.path.join(pc_prefix, pc_folder_name))
    create_folder(os.path.join(pc_prefix, pc_folder_name, mobile_folder_name))
    create_folder(os.path.join(pc_prefix, pc_folder_name, date))

    adb('adb pull {} {}'.format(
        os.path.join(mobile_prefix, mobile_folder_name),
        os.path.join(pc_prefix, pc_folder_name)
    ))
    print('Download success.')

    for filename in os.listdir(os.path.join(pc_prefix, pc_folder_name, mobile_folder_name)):
        shutil.move(
            os.path.join(pc_prefix, pc_folder_name, mobile_folder_name, filename),
            os.path.join(pc_prefix, pc_folder_name, date, filename)
        )
    os.removedirs(os.path.join(pc_prefix, pc_folder_name, mobile_folder_name))
    print('Files are moved to the folder naming with date.')

    print('Download time: {}'.format(time.time() - start_time))
    print('------------------------------------------------------------------')

    # if flag_delete:
    #     adb('adb shell rm -r {}'.format(os.path.join(mobile_prefix, mobile_folder_name)))
    #     print('Delete success.')


if __name__ == '__main__':
    download_files('/sdcard/DCIM/', 'Camera', 'Files/', 'Camera')
    download_files('/sdcard/DCIM/', 'Screenshots', 'Files/', 'Screenshots')
    download_files('/sdcard/DCIM/', 'ScreenRecorder', 'Files/', 'ScreenRecorder')
    download_files('/sdcard/MIUI/', 'sound_recorder', 'Files/', 'SoundRecorder')
    download_files('/sdcard/', 'Movies', 'Files/', 'Movies')
    download_files('/sdcard/', 'Pictures', 'Files/', 'Pictures')
    download_files('/sdcard/Tencent/', 'QQ_Images', 'Files/', 'QQ_Images')
