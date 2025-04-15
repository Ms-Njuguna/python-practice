from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    name = "Patricia"

    # List of books
    books = ['Python Basics', 'Flask for Beginners', 'Data Science with Python']
    
    # Dictionary with book details
    book_details = {
        'Python Basics': {'author': 'John Doe', 'year': 2021},
        'Flask for Beginners': {'author': 'Jane Smith', 'year': 2022},
        'Data Science with Python': {'author': 'Alice Brown', 'year': 2020}
    }

    return render_template('index.html', user_name=name, books=books, book_details=book_details)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    user = request.form['username']
    comment = request.form['comment']
    return render_template('thankyou.html', user=user, comment=comment)

if __name__ == '__main__':
    app.run(debug=True)
