from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random

app = Flask(__name__,static_folder='static')

words_with_hints = [
    ('hangman', 'A game where you guess letters to form a word.'),
    ('example', 'A thing characteristic of its kind or illustrating a general rule.'),
    ('python', 'A high-level programming language.'),
    ('flask', 'A micro web framework written in Python.'),
    ('javascript', 'A scripting language primarily used for web development.'),
    ('coding', 'The process of designing and building an executable computer program.'),
    ('apple', 'A red or green fruit with a sweet or tart taste.'),
    ('dog', 'A furry domesticated mammal, often kept as a pet.'),
    ('cat', 'A small carnivorous mammal often kept as a pet.'),
    ('sun', 'The star at the center of our solar system.'),
    ('moon', 'The natural satellite of Earth.'),
    ('algorithm', 'A step-by-step procedure or formula for solving problems.'),
    ('database', 'A structured set of data held in a computer, typically organized for rapid search and retrieval.'),
    ('network', 'A group of interconnected computers or other devices.'),
    ('interface', 'A point where two systems, subjects, organizations, etc., meet and interact.'),
    ('variable', 'A storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value.'),
    ('iteration', 'The repetition of a process or utterance.'),
    ('boolean', 'A data type with one of two possible values: true or false.'),
    ('framework', 'A set of tools, libraries, and conventions for building and structuring software.'),
    ('abstraction', 'The process of removing or suppressing details to create a simplified, higher-level representation.'),
    ('recursion', 'The process in which a function calls itself directly or indirectly.'),
    ('book', 'A set of written or printed pages, usually bound with a protective cover.'),
    ('tree', 'A tall plant with a trunk and branches made of wood.'),
    ('flower', 'The reproductive part of a plant, often colorful and fragrant.'),
    ('bird', 'A warm-blooded vertebrate with feathers and wings.'),
    ('fish', 'A limbless cold-blooded vertebrate with gills and fins.'),
    ('car', 'A road vehicle with an engine and four wheels.'),
    ('house', 'A building for human habitation.'),
    ('beach', 'A shore of a body of water covered by sand, gravel, or larger rock fragments.'),
    ('sunrise', 'The time when the sun appears above the horizon in the morning.'),
    ('river', 'A natural flowing watercourse, usually freshwater, flowing towards an ocean, sea, lake, or another river.'),
    ('cloud', 'A visible mass of water droplets or ice crystals suspended in the atmosphere.'),
     ('debugging', 'The process of finding and fixing errors in a computer program.'),
    ('encryption', 'The process of converting information into a code to prevent unauthorized access.'),
    ('star', 'A luminous celestial body that appears as a point of light in the night sky.'),
    ('moonlight', 'The light from the moon.'),
    ('planet', 'A celestial body moving in an elliptical orbit around a star.'),
    ('rain', 'Water falling in drops from the atmosphere.'),
    ('snow', 'Frozen water vapor falling to the ground in white flakes.'),
    ('ocean', 'A large expanse of sea, typically larger than a sea.'),
    ('sky', 'The region of the atmosphere and outer space seen from the earth.'),
    ('happy', 'Feeling or showing pleasure or contentment.'),
    ('sad', 'Feeling or showing sorrow; unhappy.'),
    ('funny', 'Causing laughter or amusement; humorous.'),
    ('friend', 'A person whom one knows and with whom one has a bond of mutual affection.'),
    ('family', 'A group consisting of parents and children living together in a household.'),
    ('holiday', 'A day of festivity or recreation when no work is done.'),
    ('smile', 'Form one\'s features into a pleased, kind, or amused expression, typically with the corners of the mouth turned up and the front teeth exposed.'),
    ('laugh', 'Make the spontaneous sounds and movements of the face and body that are the instinctive expressions of lively amusement and sometimes also of contempt or derision.'),
    ('sleep', 'A condition of body and mind that typically recurs for several hours every night, in which the nervous system is inactive, the eyes closed, the postural muscles relaxed, and consciousness practically suspended.'),
    ('eat', 'Put (food) into the mouth and chew and swallow it.'),
    ('drink', 'Take (a liquid) into the mouth and swallow.'),
    ('run', 'Move at a speed faster than a walk, never having both or all the feet on the ground at the same time.'),
    ('jump', 'Push oneself off a surface and into the air by using the muscles in one\'s legs and feet.'),
    ('dance', 'Move rhythmically to music, typically following a set sequence of steps.'),
    ('sing', 'Make musical sounds with the voice, especially words with a set tune.'),
    ('read', 'Look at and comprehend the meaning of written or printed matter by interpreting the characters or symbols of which it is composed.'),
    ('write', 'Mark (letters, words, or other symbols) on a surface, typically paper, with a pen, pencil, or similar implement.'),
    ('draw', 'Produce (a picture or diagram) by making lines and marks on paper with a pencil, pen, etc.'),
    ('color', 'The property possessed by an object of producing different sensations on the eye as a result of the way the object reflects or emits light.'),
    ('listen', 'Give one\'s attention to a sound.'),
    ('speak', 'Utter words so as to convey information, an opinion, a feeling, etc.'),
    ('learn', 'Gain or acquire knowledge of or skill in (something) by study, experience, or being taught.'),
    ('play', 'Engage in activity for enjoyment and recreation rather than a serious or practical purpose.'),
    ('watch', 'Look at or observe attentively over a period of time.'),
    ('work', 'Activity involving mental or physical effort done in order to achieve a purpose or result.'),
    ('study', 'The devotion of time and attention to gaining knowledge of an academic subject.'),
    ('exercise', 'Activity requiring physical effort, carried out to sustain or improve health and fitness.'),
    ('hobby', 'An activity done regularly in one\'s leisure time for pleasure.'),
    ('art', 'The expression or application of human creative skill and imagination, typically in a visual form such as painting or sculpture, producing works to be appreciated primarily for their beauty or emotional power.'),
    ('music', 'Vocal or instrumental sounds (or both) combined in such a way as to produce beauty of form, harmony, and expression of emotion.'),
    ('movie', 'A story or event recorded by a camera as a set of moving images and shown in a theater or on television; a motion picture.'),
    ('game', 'A form of play or sport, especially a competitive one played according to rules and decided by skill, strength, or luck.'),
    ('computer', 'An electronic device for storing and processing data, typically in binary form, according to instructions given to it in a variable program.'),
    ('internet', 'A global computer network providing a variety of information and communication facilities, consisting of interconnected networks using standardized communication protocols.'),
    ('email', 'Messages distributed by electronic means from one computer user to one or more recipients via a network.'),
    ('social media', 'Websites and applications that enable users to create and share content or to participate in social networking.'),
    ('video', 'The recording, reproducing, or broadcasting of moving visual images.'),
    ('camera', 'A device for recording visual images in the form of photographs, film, or video signals.'),
    ('phone', 'A telephone.'),
    ('friendship', 'The emotions or conduct of friends; the state of being friends.'),
    ('kindness', 'The quality of being friendly, generous, and considerate.'),
    ('happiness', 'The state of being happy.'),
    ('sadness', 'The condition or quality of being sad.'),
    ('knowledge', 'Facts, information, and skills acquired through experience or education; the theoretical or practical understanding of a subject.'),
    ('wisdom', 'The quality of having experience, knowledge, and good judgment; the quality of being wise.'),
    ('peace', 'Freedom from disturbance; tranquility.'),
    ('love', 'An intense feeling of deep affection.'),
    ('dream', 'A series of thoughts, images, and sensations occurring in a person\'s mind during sleep.'),
    ('adventure', 'An unusual and exciting or daring experience.')
]

# Function to create the database table
# Function to create the database table
def create_table():
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite error during table creation: {e}")
    finally:
        conn.close()


@app.route('/')
def initial_page():
    return render_template('starting.html')

@app.route('/start', methods=['POST'])
def start():
    # Perform any necessary processing before redirecting (if needed)
    # Redirect to the login page
    return render_template('login.html')

# Route for creating an account
@app.route('/create_account', methods=['GET'])
def create_account():
    return render_template('create_account.html')

# Route for handling account creation form submission
@app.route('/create_account', methods=['POST'])
def create_account_post():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return render_template('login.html')
    except sqlite3.IntegrityError:
        conn.close()
        return "Username already exists. Please choose a different one."


# Route for handling login form submission
@app.route('/login', methods=['GET' , 'POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        # Successful login - Redirect to Hangman game page
        return redirect(url_for('hangman_game'))
    else:
        return "Invalid username or password. Please try again."

# Route to serve Hangman game page
@app.route('/hangman')
def hangman_game():
    return render_template('hangman.html')

# Route to fetch a random word from the server
@app.route('/get_random_word')
def get_random_word():
    random_word, hint = random.choice(words_with_hints)
    return {'random_word': random_word, 'hint': hint}

# Route for the About page
@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard_page():
    return render_template('dashboard.html')

if __name__ == '__main__':
    create_table()  # Create the database table if it doesn't exist
    app.run(debug=True)
