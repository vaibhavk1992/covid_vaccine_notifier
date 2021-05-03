#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from vaccineNotifier import *

sched = BackgroundScheduler(daemon=True)
sched.add_job(call_initiate,'interval',seconds=10)
sched.start()

app = Flask(__name__)

@app.route("/")
def home():
    """ Function for test purposes. """
    return "COVID-19 vaccine notifier is running :) !"

if __name__ == "__main__":
    app.run()