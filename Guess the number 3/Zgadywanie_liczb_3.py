from flask import Flask, render_template, request, redirect

app = Flask(__name__)

guess_count = 1
@app.route('/', methods=['GET', 'POST'])
def zgaduj():
    """User thinks of a number between 1 and 1000.
    by providing hints (too small/too big/right) computer tries to guess the number.
    :return: html code with answers and hints
    """
    global guess_count
    if request.method == 'GET':
        return render_template('baza.html')
    if request.method == 'POST':
        if request.form['odpowiedz'] == 'OK!':
            min = 0
            max = 1000
            guess = int((max - min) / 2 + min)
            return render_template('guessing.html', answer=guess, min=min, max=max, guess_count=guess_count)

        if request.form['odpowiedz'] == 'Too small':
            min = int(request.form['answer'])
            max = int(request.form['max'])
            guess = int((max - min) / 2 + min)
            guess_count += 1
            return render_template('guessing.html', answer=guess, min=min, max=max, guess_count=guess_count)
        if request.form['odpowiedz'] == 'Too big':
            min = int(request.form['min'])
            max = int(request.form['answer'])
            guess = int((max - min) / 2 + min)
            guess_count += 1
            return render_template('guessing.html', answer=guess, min=min, max=max, guess_count=guess_count)
        if request.form['odpowiedz'] == "You win":
            return render_template('wygrana.html', guess_count=guess_count)
        if request.form['odpowiedz'] == "Again?":
            return redirect('/again')

@app.route('/again', methods=['POST', 'GET'])
def again():
    global guess_count

    guess_count = 1
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)