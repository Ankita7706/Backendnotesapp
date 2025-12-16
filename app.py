from flask import Flask, render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']= '9b141dc7726200c03ec831951f595416'

posts=[
    {
        'author':'ana huang',
        'title':'twisted love',
        'genre':'dark rom',
        'trope':'brother bestfriend , billionare'
    },
    {
        'author':'rebeccah yarros',
        'title':'fourth wing',
        'genre':'fantasy',
        'trope':'enemies to lovers'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/add_note")
def add_note():
    return render_template('add_note.html',title='Add Note')

@app.route("/edit_note")
def edit_note():
    return render_template('edit_note.html')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'ankitadutta@gmail.com' and form.password.data =='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessful. please check username and password','danger')
    return render_template('login.html',title='Login',form=form)

if __name__ == "__main__":
    app.run(debug=True)