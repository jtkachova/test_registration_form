# test_registration_form

web panel for testing registration forms on web sites. Application generates fake First names, last names and email with using testdata library and generate POST request to site.

###Requirments

-Python

-pip

Flask==0.10.1

Flask-DebugToolbar==0.10.0

Flask-WTF==0.12

Jinja2==2.8

MarkupSafe==0.23

WTForms==2.0.2

Werkzeug==0.10.4

argparse==1.2.1

blinker==1.4

fake-factory==0.2

itsdangerous==0.24

python-testdata==1.0.5

requests==2.7.0

wsgiref==0.1.2


###Installation

pip -r requirments.txt

##Run app

python app.py

Application starts on port 5000

##Configuration

Default data for POST request specified in app.py line 25. You can edit data-input variable to ajust for your POST request.

###Usage

In 127.0.0.1:5000  you'll should specify url and number of users , which will register. After submit button you'll see messages with status code, reason and text.
