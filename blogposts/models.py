from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=200, unique=True)
    img_url = models.URLField()
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    blog = models.ForeignKey(BlogPost, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.body




# class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(250), unique=True, nullable=False)
#     password = db.Column(db.String(250), nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     posts = relationship("BlogPost", backref="author")
#     comments = relationship("Commnet", backref="author")


# class BlogPost(db.Model):
#     __tablename__ = "blog_posts"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     comments = relationship("Commnet", backref="blogpost")


# class Commnet(db.Model):
#     __tablename__ = "comments"
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text, nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     blogpost_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))