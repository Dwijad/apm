from flask import Flask, render_template
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)
  
app.config['ELASTIC_APM'] = {
          'SERVICE_NAME': 'FlaskApp',
          'SECRET_TOKEN': '',
          'SERVER_URL': 'http://localhost:8200',
}

apm = ElasticAPM(app)

@app.route('/')

def index():
 return "Hello World!"

@app.errorhandler(404)
def not_found_error(error):
 return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
 return render_template('500.html'), 500

@app.route('/divbyzero')          
def divbyzero():             
    num = 2 / 0              
    return "hello world - " + str(num)

if __name__ == '__main__':
 app.run(host='172.104.163.76', port=5000)

