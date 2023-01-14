from flask import Flask, request, render_template, redirect
import random
from kostka_do_gry import rzut

app = Flask(__name__)

kostki = ("D100", "D20", "D12", "D10", "D8", "D6", "D4", "D3")

def game_roll(roll, score):
    """
        :param roll: new roll made by user/computer
        :param score: old score
        :return: new score
        """
    if roll == 7:
        score = round(score / roll)
        return score
    elif roll == 11:
         score = score * roll
         return score
    else:
        score += roll
        return score

@app.route('/', methods=['GET', 'POST'])
def start():
    """Start of the website. Explains the rules

    :return: index or start of the game
    """
    if request.method == 'GET':
        return render_template('index.html')
    else: #POST
        return redirect('/gra')
@app.route('/gra', methods=['GET', 'POST'])
def gra():
    """Main function of the app.
    lets player decide on type of dice they want to use.
    rolls for computer
    adds results together

    :return: website presenting results / winners
    """
    if request.method == 'GET':
        return render_template('gra.html', player_score=0, computer_score=0)
    else: #POST
        try:
            player_score = int(request.form.get('player_score'))
            computer_score = int(request.form.get('computer_score'))
        except TypeError:
            return render_template('gra.html', player_score=0, computer_score=0)
        dice_type = request.form['dice_type']
        player_roll = rzut(f"2{dice_type}")
        player_score = game_roll(player_roll, player_score)

        computer_dice = random.choice(kostki)
        computer_roll = rzut(f"2{computer_dice}")
        computer_score = game_roll(computer_roll, computer_score)

        if player_score >= 2001:
            return render_template('/wygrana.html', winner='Player')

        elif computer_score >= 2001:
            return render_template('/wygrana.html', winner='Computer')
        else:
            return render_template('gra.html', player_score=player_score, computer_score=computer_score)

@app.route('/wygrana', methods=['GET', 'POST'])
def wygrana():
    """Presents who won and ask user if they would like to start over.

    :return: website with a game from start
    """
    if request.method == 'POST':
        return redirect('/gra')

if __name__ == "__main__":
    app.run(debug=True)