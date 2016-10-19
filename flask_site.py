from flask import Flask, redirect, url_for, send_file, render_template, session, flash, request, send_from_directory
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from build_output import build_output
import config
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = config.secret_key

class DateForm(Form):
    date = StringField('Enter Start Date', validators=[DataRequired()])
    submit = SubmitField('Next')


class FileForm(Form):
    sheet = FileField('Upload a Template', validators=[DataRequired()])
    submit = SubmitField('Make a Schedule')


@app.route('/', methods=['GET', 'POST'])
def home_page():
    form = DateForm()
    if form.validate_on_submit():
        session['date'] = form.date.data
        form.date.data = ''
        return redirect(url_for('upload', date=session.get('date')))
    return render_template('index.html', form=form, date=session.get('date'))


@app.route('/<date>', methods=['GET', 'POST'])
def upload(date):
    u_form = FileForm()
    if u_form.validate_on_submit():
        file = u_form.sheet.data
        filename = os.path.abspath('001.xlsx')
        file.save(filename)
        build_output(folder=os.getcwd(), filename='001.xlsx', startdate=date, template_file=filename)
        return send_from_directory(filename='002.xlsx', directory=os.getcwd())
    return render_template('upload.html', form=u_form, file=session.get('file'))


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)