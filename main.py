from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session, redirect
from datetime import datetime
import json, os, math
from flask_mail import Mail
from werkzeug.utils import secure_filename

with open("config.json", 'r') as c:
    params = json.load(c)["params"]



local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)
if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
db = SQLAlchemy(app)

class Contacts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(15), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Posts(db.Model):

    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    subheading = db.Column(db.String(50), nullable=False)
    tagline = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    if "user" in session and (session['user']==params['admin_user'] or session['user']==params['gen_user']):
        posts = Posts.query.all()
        last = math.ceil(len(posts)/int(params['no_of_posts']))
        page = request.args.get('page')
        if (not str(page).isnumeric()):
            page = 1
        page = int(page)
        posts = posts[(page-1)*int(params['no_of_posts']):(page-1)*int(params['no_of_posts'])+ int(params['no_of_posts'])]
        if page==1:
            prev = "#"
            next = "/?page="+ str(page+1)
        elif page==last:
            prev = "/?page="+ str(page-1)
            next = "#"
        else:
            prev = "/?page="+ str(page-1)
            next = "/?page="+ str(page+1)
        
        return render_template('index.html', params=params, posts=posts, prev=prev, next=next)
    
    return render_template('login.html', params=params)

@app.route("/index")
def index():
    if "user" in session and (session['user']==params['admin_user'] or session['user']==params['gen_user']):
        posts = Posts.query.all()[0:params['no_of_posts']]
        return render_template('index.html', params=params, posts=posts)
    return render_template('login.html', params=params)

@app.route("/about")
def about():
    if "user" in session and (session['user']==params['admin_user'] or session['user']==params['gen_user']):
        return render_template('about.html', params=params)
    return render_template('login.html', params=params)

@app.route("/dashboard",  methods=['GET', 'POST'])
def dashboard():
    
    if ("user" in session and session['user']==params['admin_user']):
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts = posts)
    
    if request.method=='POST':
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if (username==params['admin_user'] and userpass==params['admin_password']):
            # set the session variable
            session['user']=username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
        if (username==params['gen_user'] and userpass==params['gen_password']):
            # set the session variable
            session['user']=username
            posts = Posts.query.all()[0:params['no_of_posts']]
            return render_template('index.html', params=params, posts=posts)
    
    return render_template('login.html', params=params)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if "user" in session and session['user']==params['admin_user']:
        if request.method=="POST":
            box_title = request.form.get('title')
            subheading = request.form.get('subheading')
            tline = request.form.get('tagline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            img_file = request.form.get('img_file')
            date = datetime.now()
            
            if sno=='0':
                post = Posts(title=box_title, subheading=subheading, tagline=tline, slug=slug, content=content, img_file=img_file, date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/dashboard')
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.box_title = box_title
                post.tagline = tline
                post.slug = slug
                post.content = content
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/dashboard')

        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)       

@app.route("/delete/<string:sno>" , methods=['GET', 'POST'])
def delete(sno):
    if "user" in session and session['user']==params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect("/dashboard")

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():
    if "user" in session and session['user']==params['admin_user']:
        if request.method=='POST':
            f = request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
            return "Uploaded successfully!"

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if "user" in session and (session['user']==params['admin_user'] or session['user']==params['gen_user']):
        if request.method == 'POST':
            ''' Add entry to the database'''
            name = request.form.get('name')
            email = request.form.get('email')
            phone = request.form.get('phone')
            message = request.form.get('message')
            mail.send_message('new message from ' + name, sender=email, recipients=[params['gmail-user']], body=message + "\n" + phone)
            entry = Contacts(name=name, phone_num=phone, msg=message, date=datetime.now(), email=email)
            db.session.add(entry)
            db.session.commit()

        return render_template('contact.html', params=params)
    return render_template('login.html', params=params)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    if "user" in session and (session['user']==params['admin_user'] or session['user']==params['gen_user']):
        post = Posts.query.filter_by(slug=post_slug).first()
        return render_template('post.html', params=params, post=post)
    return render_template('login.html', params=params)
app.run(debug=True)
