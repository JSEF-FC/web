from flask import Flask,render_template,request

app=Flask(__name__,template_folder='templates2')

@app.route()
def test():
  return render_template('test.html')

if __name__=="__main__":
  app.run()
