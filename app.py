from flask import Flask, render_template, url_for, request, abort
import json
import random

# json file
q = open('data.json') # open file
questions = q.read() # reads, initial type str
question_object = json.loads(questions) # convert to type list

# create flask app
app = Flask(__name__)

width = 0

# home route and view
@app.route('/', methods=['GET','POST'])
def home():
    global width
    result = '' # would also raise referenced before assignment error if not declared

    ran_count = random.randrange(len(question_object)) # random number between 0 and total # of entries in question_object list

    quote_item = question_object[ran_count] # main quote item (dict with 'text' and 'author')
    quote_text = quote_item['text']
    quote_answer = quote_item['author']

    if request.method == 'POST':
        answer = request.form.get('answer') # get the user input

        if answer.lower() == quote_item['author'].lower():
            result = 'Correct :)'
            width += 10

        else:
            result = 'Incorrect :"('
        
        print(answer.lower(), quote_item['author'].lower())
        print(quote_item)
        print(width)
        
    return render_template('index.html', quote_text = quote_text, quote_answer = quote_answer, result = result, width_dynamic = width)

if __name__ == '__main__':
    app.run(debug=True)