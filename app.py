from flask import Flask, render_template, url_for, request

app = Flask(__name__)

answer_list = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        answer = request.form.get('answer')
        answer_list.append(f'{answer}')
        
    return render_template('index.html', answer_list = answer_list)

if __name__ == '__main__':
    app.run(debug=True)