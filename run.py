from flask import Flask
from server import create_app
import config

app = create_app('config')

app.run(host = '0.0.0.0')