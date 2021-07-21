import datetime

from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
from flask import g

from . import db   ###for database

bp = Blueprint("pets", "pets", url_prefix="")

def format_date(d):
    if d:
        d = datetime.datetime.strptime(d, '%Y-%m-%d')
        v = d.strftime("%a - %b %d, %Y")
        return v
    else:
        return None



    
    

@bp.route("/",methods=['POST','GET'])
def dashboard():
    conn=db.get_db()
    cursor=conn.cursor()

    if request.method == 'POST':
        task_content=request.form.get('content')
        print(task_content)
        cursor.execute("INSERT INTO todo (content) VALUES (?)", [task_content])
        conn.commit()
        return redirect('/')
        

    else:
        cursor.execute("select content,date_created from todo order by date_created")

        tasks = (x[0] for x in cursor.fetchall())
        date_created=datetime.date.today()
        print(tasks)
        print(tasks)
        data = dict(
            
                    tasks = tasks,
                    date_created=date_created)

    return render_template('index.html', **data)
