import subprocess
import schedule
import datetime
import os

# 主机名, 用户名, ip或绑定的域名


def backupLinux(user, host):
    dirs = os.path.join(os.getcwd(), 'backup_data', user+'-'+host, str(datetime.datetime.now().year) +
                        '-' + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day))
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    cmd = ["rsync", "-azvvv",  "--bwlimit=100",  "--append-verify", user+"@"+host+":/" ,  dirs]
    subprocess.run(cmd)


while True:
    info_list = [
        {
            "user": "root",
            "host": "v2fy.com"
        }
    ]

    for value in info_list:
        schedule.every().day.at("18:25").do(backupLinux, user = value["user"], host = value["host"])
        schedule.run_pending()
