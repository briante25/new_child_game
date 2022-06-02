from flask import Flask, render_template, request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5432/testdb'
db = SQLAlchemy(app)

@app.route("/Delete/<string:id>")
def Delete(id):
    sql=f'''
    DELETE FROM english WHERE id={id}
    '''
    db.engine.execute(sql)
    return redirect(url_for('hello_world'))


@app.route("/insert", methods=["POST"])
def insert():
    question = request.values.get("question")
    ##記得用單引號##
    sql = f'''
        INSERT INTO english(question) VALUES('{question}') 
    '''
    db.engine.execute(sql)
    return "完成英文單字建檔作業：" + question


@app.route("/", methods=['POST', 'GET']) #切入網站時用GET
def hello_world():
    if request.method == "POST":
        question = request.values.get("question")
        question_url = request.values.get("question_url")
        ##--------記得用單引號--------##
        sql = f'''
            INSERT INTO english(question,question_url) VALUES('{question}','{question_url}') 
        '''
        db.engine.execute(sql)
    
    sql = f'''
        SELECT * FROM english ORDER BY id DESC
        '''
    rec = db.engine.execute(sql)
    data = list(rec)

    return render_template('form.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)
