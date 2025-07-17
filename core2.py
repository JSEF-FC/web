from flask import Flask,render_template,request

app=Flask(__name__,template_folder='templates2')

@app.route('/test',methods=['GET','POST'])
def test():
  if request.method == 'GET':
    file = request.form.get('file')
    sex1 = request.form.get('1')
    sex2 = request.form.get('2')
    a = request.form.get('a')
    b = request.form.get('b')
    c = request.form.get('b')
    print(file,sex1,sex2,a,b,c)
    return 'Successful!'
  else:
    return render_template('test.html')

if __name__=="__main__":
  app.run()
