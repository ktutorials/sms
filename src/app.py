from flask import Flask, Blueprint, request, abort, render_template
from flask_restplus import Resource, Api, Namespace
from sms.src.lib import db

api_bp = Blueprint('api', __name__, url_prefix='/api')
v1_ns = Namespace('v1', description='students api resources')

api = Api(api_bp, version='1.0', title='Students API',description='Students API resources')
api.add_namespace(v1_ns)

app_path = "/Users/psanyal/PycharmProjects/sample/sms/"
app = Flask(__name__,
            static_url_path='',
            static_folder="{0}static".format(app_path),
            template_folder="{0}templates".format(app_path))
app.register_blueprint(api_bp)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

'''
@api.route('/helloworld')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


@api.route('/hello/<string:name>')
class HelloName(Resource):
    def get(self, name):
        return {'hello': name}
'''


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html', abc="param")


@v1_ns.route('/students')
class Students(Resource):
    def get(self):
        return db.get_students()

    def post(self):
        if request.json:
            result, err = db.add_student(request.json)
            if err:
                return {'success': result, 'error': str(err)}
            return {'success': result}
        else:
            abort(400, "Missing student data.")


if __name__ == '__main__':
    app.run(debug=True)
