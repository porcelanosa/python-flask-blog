import sys
import os

activate_this = '/var/www/porcelanosa/data/www/in.71b.ru/newenv/bin/activate_this.py'

with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# sys.path.append('/usr/local/lib/python3.4/dist-packages/')
# sys.path.append('/var/www/porcelanosa/data/www/in.71b.ru/venv/')
# sys.path.append(' /var/www/porcelanosa/data/www/in.71b.ru/venv/Lib/site-packages/')
sys.path.insert(0, '/var/www/porcelanosa/data/www/in.71b.ru')
# sys.path.insert(0, '/var/www/porcelanosa/data/www/in.71b.ru/dream_team_app/dream_team_app')
sys.path.insert(0, '/var/www/porcelanosa/data/www/in.71b.ru/dream_team_app')
sys.path.insert(0, '/var/www/porcelanosa/data/www/in.71b.ru/dream_team_app/run.py')

os.environ['FLASK_CONFIG'] = 'production'

# print(sys.version)
# print(sys.path)
# print (os.getcwd())


from dream_team_app.run import app as application
