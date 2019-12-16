from flask import Flask
#from flask_mongoengine import MongoEngine
#from flask_admin import Admin
#from flask_admin.form import rules
#from streamer.models import Camera
#import pymongo

#class mongo_connection:
#  conn = None
#
#  def connect(self):
#    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#    mydb = myclient["tracker"]
#    self.conn = mydb["restaurants"]
#    return self.conn
#
#  def query(self, sql):
#      cursor = self.conn.find(sql)  
#      return cursor 
#
#dbcon = mongo_connection()
#db = dbcon.connect()
#

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')
    
    # apply overrides for tests
    app.config.update(config_overrides)
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    
    #admin = Admin(app, name='streamer',template_mode='bootstrap3')
    
    # setup db
    #db.init_app(app)

    from base.views import base_app
    #from manage.views import manage_app

    app.register_blueprint(base_app)
    #app.register_blueprint(manage_app)

    return app
