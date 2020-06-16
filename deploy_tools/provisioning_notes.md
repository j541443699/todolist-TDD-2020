Provisioning a new site

==============================

## Required packages:

* nginx
* Python 3.6 + pip
* virtualenv 
* Git

eg, on CentOS:

### Install Nginx

谷歌搜索centos安装nginx即可。

```
//相关命令
sudo systemctl start nginx	//启动nginx
sudo systemctl stop nginx
sudo systemctl restart nginx
```

### Install python3.6

```
//root模式下进行，
yum install epel-release //安装EPEL
yum install https://centos7.iuscommunity.org/ius-release.rpm //安装IUS软件源（装python3.6时涉及到的步骤，实际上这一步不需要，直接跳过）。这一步执行后，会卡住，因为该国外网址无法访问
yum install python3	//这里同时安装python3和pip3
```

其他的包直接搜索安装即可。

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., 123.123.123.123

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., 123.123.123.123

## Folder structure

Assume we have a user account at /home/username

/home/username
    └── data
        └── TDD-2020
            └── sites
                └── SITENAME
                    ├── database
                    │   └── db.sqlite3
                    ├── source
                    │   ├── deploy_tools
                    │   ├── functional_tests
                    │   ├── lists
                    │   ├── manage.py
                    │   ├── requirements.txt
                    │   └── superlists
                    ├── static
                    │   ├── base.css
                    │   └── bootstrap
                    └── virtualenv
                        ├── bin
                        ├── include
                        ├── lib
                        ├── lib64 -> lib
                        ├── pip-selfcheck.json
                        └── pyvenv.cfg