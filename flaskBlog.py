"""from flask import Flask,render_template, redirect, url_for
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html')

@app.route("/otrohome")
def otrohome():
   return redirect("http://localhost:5000/")

@app.route("/my/<username>/<int:edad>")
def my(username,edad):
   return "<h1>You're returning: "+username+ "Edad : "+str(edad)+"</h1>"
#For dynamic url:  url_for

@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('home', username=uname))

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)"""

from flask import Flask,render_template, redirect, url_for
app = Flask(__name__)
# This variable acts as I have a json
myPosts = [
  {
    'author':'Chuyo',
    'title':'Blog Post 1',
    'content':'First post',
    'date_posted':'April 20, 2018'
  },
  {
    'author':'Rupert',
    'title':'Blog Post 2',
    'content':'Second post',
    'date_posted':'June 19, 2018'
  }
]

@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html', posts = myPosts)

@app.route("/about")
def about():
   return render_template('about.html', title = 'My about')


@app.route("/otrohome")
def otrohome():
   return redirect("http://localhost:5000/")

@app.route("/my/<username>/<int:edad>")
def my(username,edad):
   return "<h1>You're returning: "+username+ "Edad : "+str(edad)+"</h1>"
#For dynamic url:  url_for

@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('home', username=uname))

if __name__ == '__main__':
    #app.run()
    app.run(debug=True)


"""
from flask import Flask
import random
## Define a flask application name 'app' below

app = Flask(__name__)

## Define below a view function 'hello', which displays the message 
## "Hello World!!! I've run my first Flask application."
## The view function 'hello' should be mapped to URL '/' .
@app.route("/")
@app.route("/hello")
def hello():
   return "Hello World!!! I've run my first Flask application."


## Define below a view function 'hello_user', which takes 'username' as an argument 
## and returns the html string containing a 'h2' header  "Hello <username>"
## After displaying the hello message, the html string must also display one quote, 
## randomly chosen from the provided list `quotes` 
## Before displaying the quote, the html string must contain the 'h3' header 'Quote of the Day for You' 
## The view function 'hello_user' should be mapped to URL '/hello/<username>/' .
## Use the below list 'quotes' in 'hello_user'  function

@app.route("/hello/<username>/")
def hellouser(username):
    quotes = ["Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "Listen to many, speak to a few.",
                "Only when the tide goes out do you discover who has been swimming naked."
    ]
    r =random.randint(0,4)
    message = "<h2>hello "+ username+"</h2> Quote of the day for you: "+ quotes[r]+""
    return message


## Define below a view function 'display_quotes', which returns an html string 
## that displays all the quotes present in 'quotes' list in a unordered list.
## Before displaying 'quotes' as an unordered list, the html string must also include a 'h1' header "Famous Quotes".
## The view function 'display_quotes' should be mapped to URL '/quotes/' .
## Use the below list 'quotes' in 'display_quotes'  function
## quotes = [
##                "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
##                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
##                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
##                "Listen to many, speak to a few.",
##                "Only when the tide goes out do you discover who has been swimming naked."
##    ]
@app.route("/quotes/")
def display_quotes():
    quotes = ["Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
                "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
                "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
                "Listen to many, speak to a few.",
                "Only when the tide goes out do you discover who has been swimming naked."
    ]
    disorderQuotes = random.sample(quotes, k = len(quotes))
    q = ""
    for i in disorderQuotes:
        q =q + "<br>"+ i + "</br>"
    message = "<h1>Famouse Quotes</h1>"+ q +""
    return message

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port =8000)
## Write the required code below which runs flask applictaion 'app' defined above
## on host 0.0.0.0 and port 8000  
"""