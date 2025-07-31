
# 🎮 Hangman Web Game (with Flask & JavaScript)

This is a web-based Hangman game developed using **Python (Flask)** for the backend and **HTML/CSS/JavaScript** for the frontend. The game includes features like random word generation with hints, audio feedback, login/signup system using SQLite, and a leaderboard dashboard.

---

## 📁 Project Structure

```
project-root/
│
├── app.py                     # Main Flask application
├── users.db                   # SQLite database (auto-created)
├── README.md                  # Project overview and usage instructions
│
├── templates/                 # HTML templates for Flask
│   ├── hangman.html
│   ├── login.html
│   ├── create_account.html
│   ├── dashboard.html
│   ├── starting.html
│   └── about.html
│
├── static/                    # Static files: JS, CSS, sounds
│   ├── hangman.js             # Game logic in JavaScript
│   ├── dashboard.js           # Leaderboard functionality
│   ├── hangman.css            # CSS styles (create if not exists)
│   ├── correct.wav            # Sound for correct guesses
│   └── loss.wav               # Sound for incorrect guesses
```

---

## 🚀 How to Run the Project

### 🧑‍💻 Requirements

- Python 3.x
- Flask (`pip install flask`)

---

### 🔧 Setup Steps

1. **Clone this repository** or download the source files.

2. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

3. **Run the Flask app**:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📝 Features

- ✅ User login and account creation system
- 🧠 Random word and hint system
- ⌨️ Input letter to guess word
- 🔊 Audio feedback for correct/wrong guesses
- 📊 Leaderboard dashboard (future update-ready)
- 💡 Hints shown for each word
- 🔐 SQLite database integration

---

## 📷 Screenshots

> Add screenshots here after running the project (`/hangman`, `/login`, `/dashboard` views).

---

## ✍️ Author

**Ramisetti Praneeth**  
📧 [praneethramisetti9@gmail.com](mailto:praneethramisetti9@gmail.com)  
🌐 [LinkedIn](https://linkedin.com/in/praneeth-ramisetti354b1726a)  
💻 [GitHub](https://github.com/praneethramisetti168)

---

## 📌 Notes

- Make sure to place your `correct.wav` and `loss.wav` files in the `static/` folder.
- Create a `hangman.css` inside `static/` for custom styles.
- The SQLite database (`users.db`) is auto-created when the project first runs.

---

## 📃 License

This project is for educational and personal use only.
