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
        date_end=""
        overdue="No"
        completed=0

        cursor.execute("INSERT INTO todo (content,date_created,date_ended,over_due,completed) VALUES (?,?,?,?,?)", [task_content,date_created,date_end,overdue,completed])
        conn.commit()
        return redirect('/')
        

    else:
        cursor.execute("select * from todo order by date_created")
        data=cursor.fetchall()
        today_date=datetime.datetime.now()
        for d in data:
            created_date=datetime.datetime.strptime(d[2],"%Y-%m-%d %H:%M:%S")
            overdue=created_date+datetime.timedelta(days=7)
           
            overdue_stat1="yes"
            overdue_stat2="No"

            if overdue<today_date:
                cursor.execute("update todo set over_due=? where id=?;",(overdue_stat1,d[0]))
            else:
                cursor.execute("update todo set over_due=? where id=?;",(overdue_stat2,d[0]))

        cursor.execute("select * from todo order by date_created ")
        data=cursor.fetchall()
        

    return render_template('index.html', data=data)
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

@bp.route('/done/<int:id>')
def done(id):

    
    conn=db.get_db()
    cursor=conn.cursor()
    
    completed=1
    date_end=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    
    cursor.execute("update todo set date_ended=? where id=?;",(date_end,id))
    cursor.execute("update todo set completed=? where id=?;",(completed,id))
    conn.commit()
    return redirect('/')

@bp.route('/weekly_schedule')
def weekly_schedule():
    conn =db.get_db()
    cursor = conn.cursor()
    
    cursor.execute("select * from todo where completed=0 order by date_created")
    data=cursor.fetchall()
    
    
    return render_template('weekly_schedule.html',data=data)
@bp.route('/completed_tasks')
def completed_tasks():
    conn =db.get_db()
    cursor = conn.cursor()
    
    cursor.execute("select * from todo where completed=1 order by date_created")
    data=cursor.fetchall()
    
    
    return render_template('completed_tasks.html',data=data)
@bp.route('/clear_all')
def clear_all():
    conn =db.get_db()
    cursor = conn.cursor()
    cursor.execute("delete from todo")
    conn.commit()
    return redirect('/')