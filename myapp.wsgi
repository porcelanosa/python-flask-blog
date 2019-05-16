import sys
import os

activate_this = '/var/www/porcelanosa/data/www/blog.71b.ru/env3/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# sys.path.append('/opt/rh/rh-python36/root/usr/bin/python3.4/dist-packages/')
# sys.path.append('/var/www/porcelanosa/data/www/blog.71b.ru/venv/')
# sys.path.append(' /var/www/porcelanosa/data/www/blog.71b.ru/venv/Lib/site-packages/')
# sys.path.insert(0, '/var/www/porcelanosa/data/www/blog.71b.ru/dream_team_app/dream_team_app')


sys.path.insert(0, '/var/www/porcelanosa/data/www/blog.71b.ru')
sys.path.insert(0, '/var/www/porcelanosa/data/www/blog.71b.ru/my-blog')
sys.path.insert(0, '/var/www/porcelanosa/data/www/blog.71b.ru/my-blog/blog-run.py')

os.environ['FLASK_CONFIG'] = 'production'

# print(sys.version)
# print(sys.path)
# print (os.getcwd())


from blog import app as application
