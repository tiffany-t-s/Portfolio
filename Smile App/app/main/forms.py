from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from wtforms.validators import  ValidationError, DataRequired, Length
from app.main.models import Tag, User

from app import db
import sqlalchemy as sqla

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    happiness_level = SelectField('Happiness Level',choices = [(3, 'I can\'t stop smiling'), (2, 'Really happy'), (1,'Happy')])   
    body = TextAreaField('Body', [Length(min=1, max=1500)])
    tag = QuerySelectMultipleField('Tag', query_factory = lambda : db.session.scalars(sqla.select(Tag)), 
                                    get_label = lambda theTag : theTag.name, 
                                    widget=ListWidget(prefix_label=False), 
                                    option_widget=CheckboxInput())
    submit = SubmitField('Post')

class SortForm(FlaskForm):
    selection = SelectField('Sort By',choices= [(4, 'Date'), (3, 'Title'), (2, "# of Likes"), (1, 'Happiness Level')])
    my_posts = BooleanField('Display my posts only')
    submit = SubmitField('Refresh')
