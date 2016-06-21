#! /usr/local/bin/python
# _*_coding: utf-8

from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
import birthDB


class BirthDetailsForm(djangoforms.ModelForm):
	class Meta:
		model = birthDB.BirthDetails

	html = template.render('templates/header.html', {'title': 'Report a Possible Sighting'})
	html = html + template.render('templates/form_start.html', {})
	html = html + str(BirthDetailsForm(auto_id=False))
	html = html + template.render('templates/form_end.html', {'sub_title': 'Submit Details'})
	html = html + tempalte.render('templates/footer.html', {'link': ''})
