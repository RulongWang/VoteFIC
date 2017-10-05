# -*- coding: utf-8 -*-
import os
import sqlite3
from flask import Flask, session, redirect, url_for, escape, request,render_template,g,abort,jsonify,json

app = Flask(__name__)
app.config.from_object('config')

# @app.route("/voting", methods=["POST"])

@app.route("/voting")
def voting():
    if request.method == "POST":

        res = query_db("SELECT * FROM voting")
        print res
    return render_template('vote.html')
        # return jsonify(month=[x[0] for x in res],                  )

def get_db():
    db = sqlite3.connect(app.config['DATABASE'])
    db.row_factory = dict_factory
    return db


def query_db(query, args=(), one=False):
    db = get_db()
    cur = db.execute(query, args)
    db.commit()
    rv = cur.fetchall()
    db.close()
    return (rv[0] if rv else None) if one else rv

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d




@app.route('/')
def index():
    if 'voteid' in session:
        #check available coins for voting
        #return 'Logged in as %s' % escape(session['voteid'])
        return render_template('dashborad.html')
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if int(request.form['voteid']) not in range(1 , 201):
            print "invalid voteid"
            error = "invalid voteID"
            return render_template('login.html', error=error)

        else:
            session['voteid'] = request.form['voteid']
            return redirect(url_for('index'))
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html')



@app.route('/vote',methods=['POST', 'GET'])
def vote():
    return render_template('vote.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('voteid', None)
    return redirect(url_for('index'))


@app.route("/addVote", methods=['POST', 'GET'])
def addVote():
    error = None
    if request.method == 'POST':

        voteID = int(session["voteid"])
        ideaNum = int(request.form["ideavalue"])
        gift =int(request.form["gifttype"])
        comment = request.form["comment"]
        if gift in {1,2,3}:
            value = 3
        else:
            if gift in {4,5,6}:
                value = 2
            else:
                value = 1
        res = query_db('insert into voting values(?,?,?,?,?)',(voteID,ideaNum,gift,value,comment))
        return jsonify(res)


@app.route("/getVotes",methods=['POST','GET'])
def getVotes():
    error = None
    if session.get('voteid') == True:
        voteID = int(session['voteid'])
    else:
        #voteID = request.args.get('voterid')
        voteID = int(session['voteid'])

    if request.method == 'POST':
        rs = query_db('select ideanum,value from voting where voterid=?',(voteID,))
        print rs
        return jsonify(rs)
    else:
        rs = query_db('select ideanum,value from voting where voterid=?',(voteID,))
        return jsonify(rs)

@app.route("/reset",methods=['POST','GET'])
def reset():
    error = None
    voteID = int(session["voteid"])

    if voteID == 88:

        if request.method == 'POST':
            rs = query_db('delete *  from voting')
            print rs
            return jsonify({'status':'no success'})
        else:
            rs = query_db('delete from voting')
            return jsonify({'status':'no success'})
    else:
        return jsonify({'status':'no auth'})

@app.route("/getVoteInfo", methods=['POST', 'GET'])
def getVoteInfo():
    error = None
    result = None
    voteID = int(session["voteid"])
    vote={}
    gift={}
    if request.method == 'POST':

        voteID = int(session["voteid"])
        # ideaNum = int(request.form["ideavalue"])
        # gift =int(request.form["gifttype"])
        # comment = request.form["comment"]

        res = query_db('select * from voting where voterid= ?',(voteID,))
        result = res
    else:
        res = query_db('select * from voting where voterid= ?', (voteID,))
        res_ideanum = query_db('select ideanum from voting where voterid = ? ',(voteID,))
        res_gift = query_db('select value from voting where voterid = ? ',(voteID,))
        print res_ideanum
        print res_gift
        result = res
    for row in result:
        print row
    if not result:
        error = 'no records'
    return jsonify(result)
    # return '<br>'.join(str(re) for re in result)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')
