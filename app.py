from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators
from flask import Flask, request, session, url_for, redirect, render_template, Markup

# app settings
DEBUG = True
#DATABASE = 'data.db'
#PER_PAGE = 1000
SECRET_KEY = 'secret key!'

# create app
app = Flask( __name__ )
app.config.from_object( __name__ )

# home page
@app.route('/')
def index():
    return '''
    Siegel Lab Tools <br>
    <a href="/cm">Comparative modeling</a> -
    <a href="/active_site_energy">Active site energy</a>
    '''

# comparative modeling
class ComparativeModelingForm(FlaskForm):
  input_pdb = StringField('Input PDB', [validators.Length(max=4)])
  submit = SubmitField("Submit")

@app.route('/cm', methods=['GET', 'POST'])
def cm():
  form = ComparativeModelingForm()
  return render_template( 'cm.html', form=form )

# active site energy
class ActiveSiteEnergyForm(FlaskForm):
  input_pdb = StringField('Input PDB', [validators.Length(max=4)])
  radius = IntegerField('Radius around ligand')
  submit = SubmitField("Submit")

@app.route('/active_site_energy', methods=['GET', 'POST'])
def active_site_energy():
  form = ActiveSiteEnergyForm()
  return render_template( 'active_site_energy.html', form=form )
