from flask import Flask, redirect, url_for, render_template, session, send_from_directory, send_file
from flask_bootstrap import Bootstrap
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired
from build_output import build_output
import config
import os


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = config.secret_key


class DateForm(FlaskForm):
    date = StringField('Enter Start Date', validators=[DataRequired()], render_kw={"placeholder": "XX-XX-XX"})
    submit = SubmitField('Next')


class FileForm(FlaskForm):
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


@app.route('/<date>.xlsx', methods=['GET', 'POST'])
def upload(date):
    u_form = FileForm()
    if u_form.validate_on_submit():
        file = u_form.sheet.data
        if '.xlsx' in str(file) or '.xlm' in str(file):
            filename = os.path.abspath('001.xlsx')
            file.save(filename)
            build_output(folder=os.getcwd(), filename='001.xlsx', startdate=date, template_file=filename)
            return send_from_directory(filename='002.xlsx', directory=os.getcwd())
    return render_template('upload.html', form=u_form, file=session.get('file'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/Goodwill_schedule.xlsx')
def send_temp():
    return send_file(filename_or_fp='Goodwill_schedule.xlsx')


if __name__ == '__main__':
    app.run(debug=True)