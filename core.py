from flask import Flask,render_template,request

app= Flask(__name__,static_folder='photo')


@app.route('/show/info')
def index():
  return render_template('home_page.html')


@app.route('/python/reptile')
def reptile():
  return render_template('p_reptile.html')


@app.route('/tools/box')
def toolsbox():
  return render_template('tools_box.html')


@app.route('/sign/in',methods=['get','post'])
def signin():
  if request.method == 'get':
    return render_template('sign.html')
  else:
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    sex = request.form.get("n1")
    file = request.form.get("file")
    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('c')
    print(user, pwd, sex, file, a, b, c)

    return "Successful!"


@app.route('/register',methods=['GET','post'])
def register():
  if request.method == 'get':
    return render_template("register.html")
  else:
    user = request.form.get("user")
    pwd = request.form.get("pwd")
    sex = request.form.get("n1")
    hobby = request.form.get("hobby")
    skills = request.form.get('skills')
    more = request.form.get('signature')
    print(user, pwd, sex, hobby, skills, more)

    return "Successful!"


@app.route('/user/list')
def user_list():
  return render_template('user_list.html')

if __name__=='__main__':
  app.run(host='127.0.0.1',port=3001)


