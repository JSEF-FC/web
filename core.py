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

@app.route('/sign/in')
def signin():
  return render_template('sign.html')

@app.route('/user/list')
def user_list():
  return render_template('user_list.html')

@app.route('/register',methods=['GET'])
def register():
  return render_template("register.html")

@app.route('/storage',methods=['GET'])
def do_register():
  print(request.args)
  return "Successful!"

if __name__=='__main__':
  app.run(host='127.0.0.1',port=3001)
  '''index.run()
  reptile.run()
  toolsbox.run()
  signin.run()
  register.run()'''