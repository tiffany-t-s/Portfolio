from datetime import datetime, timezone
from typing import Optional
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin
import sqlalchemy as sqla
import sqlalchemy.orm as sqlo

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class User(UserMixin, db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    username : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(64), index = True, unique= True)
    email : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(120), index = True, unique = True)
    password_hash : sqlo.Mapped[Optional[str]] = sqlo.mapped_column(sqla.String(256))

    # #relationships
    posts : sqlo.WriteOnlyMapped['Post'] = sqlo.relationship(back_populates = 'writer')

    #methods
    def __repr__(self):
        return '<User {} - {} - {} >'.format(self.id, self.username, self.email)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_user_posts(self):
        return db.session.scalars(self.posts.select()).all()
    
    def get_post_relationship(self):
        return self.posts.select()



#A table that associates the many-to-many relationship between Post and Tag
postTags = db.Table(
    'postTags',
    db.metadata,
    sqla.Column('post_id', sqla.Integer, sqla.ForeignKey('post.id'), primary_key=True),
    sqla.Column('tag_id', sqla.Integer, sqla.ForeignKey('tag.id'), primary_key=True)
)

class Post(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    user_id : sqlo.Mapped[int] = sqlo.mapped_column(sqla.ForeignKey(User.id), index = True)
    title : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(150))
    body : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(1500))
    likes : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default = 0)
    timestamp : sqlo.Mapped[Optional[datetime]] = sqlo.mapped_column(default = lambda : datetime.now(timezone.utc)) 
    happiness_level : sqlo.Mapped[int] = sqlo.mapped_column(sqla.Integer, default = 3)
    
    #relationship
    writer : sqlo.Mapped[User] = sqlo.relationship(back_populates = 'posts')
    tags : sqlo.WriteOnlyMapped['Tag'] = sqlo.relationship(
        secondary= postTags,
        primaryjoin=(postTags.c.post_id == id),
        back_populates= 'posts',
        passive_deletes=True
    )

    #methods
    def __repr__(self):
        return '<Post - {} title: {} likes: {}>'.format(self.id, self.title, self.likes)
    
    def get_tags(self):
        query = self.tags.select()
        return db.session.scalars(query).all()


class Tag(db.Model):
    id : sqlo.Mapped[int] = sqlo.mapped_column(primary_key=True)
    name : sqlo.Mapped[str] = sqlo.mapped_column(sqla.String(20))

    #relationship
    posts : sqlo.WriteOnlyMapped['Post'] = sqlo.relationship(
        secondary= postTags,
        primaryjoin=(postTags.c.tag_id == id),
        back_populates= 'tags'
    )

    #methods
    def __repr__(self):
        return '<Tag - {} name: {}>'.format(self.id, self.name)
    
    def get_posts(self):
        query = self.posts.select()
        return db.session.scalars(query).all()




