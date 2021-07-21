import datetime
import random
import sqlite3

import click 
from flask import current_app, g
from flask.cli import with_appcontext

from faker import Faker  #for fake texts or random texts in the app






def get_db():
    if 'db' not in g: 
        dbname = current_app.config['DATABASE'] 
        g.db = sqlite3.connect(dbname)   ##############creating dtabase named DATABASE  #####3g for storing data across application contexts (((globla)))
        g.db.execute("PRAGMA foreign_keys = ON;")######foreign key constraint
    return g.db
    
    

def close_db(e=None):
    db = g.pop('db', None)  ##removing db from g
    if db is not None:
        db.close()
        
        
        

def init_db():#######initialise database
    db = get_db()
    # Create the tables
    f = current_app.open_resource("sql/000_initial.sql")###opening sqlfile
    sql_code = f.read().decode("ascii")
    
    
    cur = db.cursor()
    cur.executescript(sql_code)
    cur.close()
    db.commit()
    
    
    
    
    
    
    close_db()

@click.command('initdb', help="initialise the database")      #####some code for displaying information on terminal
@with_appcontext
def init_db_command():
    init_db()
    click.echo('DB initialised') 

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

