from config import Config

from app import create_app, db
from app.main.models import Post, Tag, User
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

app = create_app(Config)

@sqla.event.listens_for(Tag.__table__, 'after_create')
def add_tags(*args, **kwargs):
    query = sqla.select(Tag)
    if db.session.scalars(query).first() is None:
        tags = ['funny','inspiring', 'true-story', 'heartwarming', 'friendship']
        for t in tags:
            db.session.add(Tag(name = t))
        db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'sqlo': sqlo, 'db': db, 'Post': Post, 'Tag': Tag, 'User': User}

#tags = ['funny','inspiring', 'true-story', 'heartwarming', 'friendship']

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)