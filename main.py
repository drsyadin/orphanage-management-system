from flask import Flask
from public import public
from admin import admin

from OrphanageManager import OrphanageManager
from user import user

app=Flask(__name__)
app.secret_key="hii"
app.register_blueprint(public)
app.register_blueprint(admin)

app.register_blueprint(OrphanageManager)
app.register_blueprint(user)
app.run(debug=True,port=5012)