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

```
 server {
     listen 80;
     server_name 111.222.333.44; # здесь прописать или IP-адрес или доменное имя сервера
     access_log  /var/log/nginx/example.log;
  
     location /static/ {
         root /home/user/myprojectenv/myproject/myproject/;
         expires 30d;
     }
  
     location / {
         proxy_pass http://127.0.0.1:8000; 
         proxy_set_header Host $server_name;
         proxy_set_header X-Real-IP $remote_addr;
         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
     }
 }
```


gunicorn krasgk.wsgi:application --bind 127.0.0.1:8000

=======

Запуск в супервизоре: /www/env/krasgk/bin/gunicorn krasgk.wsgi:application -c /www/krasgk/krasgk/gunicorn.conf.py

cd /etc/supervisor/conf.d/
touch myproject.conf
nano myproject.conf

```
 [program:myproject]
 command=/home/user/myprojectenv/bin/gunicorn myproject.wsgi:application -c /home/user/myprojectenv/myproject/myproject/gunicorn.conf.py
 directory=/home/user/myprojectenv/myproject
 user=nobody
 autorestart=true
 redirect_stderr=true
```
