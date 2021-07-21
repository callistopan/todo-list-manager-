import datetime

from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
from flask import g

from . import db   ###for database

bp = Blueprint("pets", "pets", url_prefix="")





    
    

@bp.route("/",methods=['POST','GET'])
def dashboard():
    conn=db.get_db()
    cursor=conn.cursor()

    if request.method == 'POST':
        task_content=request.form.get('content')
        date_created=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO todo (content,date_created) VALUES (?,?)", [task_content,date_created])
        conn.commit()
        return redirect('/')
        

    else:
        cursor.execute("select * from todo order by date_created")
        data=cursor.fetchall()
    return render_template('index.html', data=data)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@bp.route('/delete/<int:id>')
def delete(id):

    print(id)
    conn=db.get_db()
    cursor=conn.cursor()
    done="activity is done"
    date_end=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("update todo set content=? where id=?;",(done,id))
    cursor.execute("update todo set date_created=? where id=?;",(date_end,id))
    conn.commit()
    return redirect('/')