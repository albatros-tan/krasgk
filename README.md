# krasgk
The site of the Krasnoyarsk mining company. The Django framework is used

Deployment:
apt install git python3-pip nginx
python3.6 -m pip install --upgrade pip
pip3 install virtualenv
mkdir /www/env
virtualenv -p python3.6 /www/env/krasgk
source /www/env/krasgk/bin/activate



git clone https://github.com/albatros-tan/krasgk.git
cd krasgk
pip install gunicorn
pip install -r requirements.txt


nano /etc/nginx/sites-available/default

1. server {
2.     listen 80;
3.     server_name 111.222.333.44; # здесь прописать или IP-адрес или доменное имя сервера
4.     access_log  /var/log/nginx/example.log;
5.  
6.     location /static/ {
7.         root /home/user/myprojectenv/myproject/myproject/;
8.         expires 30d;
9.     }
10.  
11.     location / {
12.         proxy_pass http://127.0.0.1:8000; 
13.         proxy_set_header Host $server_name;
14.         proxy_set_header X-Real-IP $remote_addr;
15.         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
16.     }
17. }



gunicorn krasgk.wsgi:application --bind 127.0.0.1:8000

=======

Запуск в супервизоре: /www/env/krasgk/bin/gunicorn krasgk.wsgi:application -c /www/krasgk/krasgk/gunicorn.conf.py

cd /etc/supervisor/conf.d/
touch myproject.conf
nano myproject.conf

1. [program:myproject]
2. command=/home/user/myprojectenv/bin/gunicorn myproject.wsgi:application -c /home/user/myprojectenv/myproject/myproject/gunicorn.conf.py
3. directory=/home/user/myprojectenv/myproject
4. user=nobody
5. autorestart=true
6. redirect_stderr=true
