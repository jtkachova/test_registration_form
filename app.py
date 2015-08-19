import testdata
import requests
from flask import Flask, render_template, request, flash
from forms import Data
app = Flask(__name__)
app.secret_key = 'key'
class Users(testdata.DictFactory):
    id = testdata.CountingFactory(1)
    firstname = testdata.FakeDataFactory('firstName')
    lastname = testdata.FakeDataFactory('lastName')
    email = testdata.FakeDataFactory('email')
def generate_request (url, data):
     r = requests.post(url, data=data)
     return r
@app.route('/', methods=['GET', 'POST'])
def load_test():
    form = Data(request.form)
    if request.method == 'POST' and form.validate():
        for user in Users().generate(form.users_number.data):
            #adjust your POST data request bellow
            data_input={'registration-email': user.get('email'), 'company_name': '',\
            'registration-firstname': user.get('firstname') , 'registration-lastname': user.get('lastname'), \
             'registration-submit': 'Join Now', 'next': form.url.data}
            url=form.url.data
            print user.get('lastname')
            r = generate_request(url, data=data_input)
            flash("user email" + user.get('email') + "\n" + "status code "+ str(r.status_code) + "\n" + "reason " + str(r.reason))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.debug = False
    app.run(debug=True)


