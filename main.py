from flask import Flask, redirect, url_for, render_template,request
app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template("home.html")

@app.route('/aboutpage')
def about_us():
   return render_template("about.html")

@app.route('/contactpage', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        print(name, email, message)  # just to check in console

        return "Message Sent Successfully!"

    return render_template("contact.html")

@app.route('/blogpage')
def blog():
   return render_template("blog.html")
if __name__ == '__main__':
   app.run()

