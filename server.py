"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
DISS_LIST = [
    'terrible', 'not-funny', 'stinky', 'awful']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <h1>Hi! This is the home page.</h1>
      <div>
          <a href="http://localhost:5000/hello">hello page</a>
      </div>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    compliment_options_str = ""
    for word in AWESOMENESS:
        compliment_options_str += f'<option value="{word}">{word}</option>'

    diss_options_str = ""
    for word in DISS_LIST:
        diss_options_str += f'<option value="{word}">{word}</option>'

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1><br>
        <h2>Pay someone a compliment:</h2><br>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br><br>
        <legend for="compliment">Select a compliment:</legend>
        <select name="compliment" id="compliment">
          {compliment_options_str}
        </select><br><br>
        <input type="submit" value="Submit">
      </fieldset>
        </form><br>

        <h2>Insult someone:</h2><br>
        <form action="/diss">
        What's your name? <input type="text" name="person"><br><br>
        <legend for="diss">Select an insult:</legend>
        <select name="diss" id="diss">
          {diss_options_str}
        </select><br><br>
        <input type="submit" value="Submit">
      </fieldset>
        </form>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/diss')
def diss_person():
    """Get diss from user."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    # compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
