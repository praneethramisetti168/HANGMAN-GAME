// hangman.js

// Game variables
var word = '';
var hint = '';
var guesses = '';
var attempts = 10;

// Function to fetch a random word with hint from Flask server
function fetchRandomWord() {
    fetch('/get_random_word')
        .then(response => response.json())
        .then(data => {
            word = data.random_word.toLowerCase();
            hint = data.hint; // Get the hint for the word
            updateWordDisplay();
            displayHint(); // Display the hint
        })
        .catch(error => console.error('Error fetching random word:', error));
}

// Function to display the hint
function displayHint() {
    document.getElementById('hint-display').textContent = `Hint: ${hint}`;
}//document obejct model -linked with tags


// Call fetchRandomWord function when the game starts (e.g., page load)
window.onload = function () {
    fetchRandomWord();
};

// Function to update the word display
function updateWordDisplay() {
    var display = '';
    for (var char of word) {
        if (guesses.includes(char)) {
            display += char;
        } else {
            display += '_ ';
        }
    }
    document.getElementById('word-display').textContent = display;
}

// Function to check if a guess is correct
function isCorrectGuess(guess) {
    return word.includes(guess);
}

// Function to make a guess
// Function to make a guess
// Function to make a guess
function makeGuess() {
    var guessInput = document.getElementById('guess-input').value.toLowerCase();

    // Check if the guess is a single letter
    if (/^[a-z]$/.test(guessInput)) {
        // Check if the guess is not already made
        if (!guesses.includes(guessInput)) {
            guesses += guessInput;

            // Check if the guess is correct
            if (!word.includes(guessInput)) {
                attempts--;
            }

            // Update word display and attempts left
            updateWordDisplay();
            document.getElementById('attempts-left').textContent = attempts;

            // Check if the player won
            if (!document.getElementById('word-display').textContent.includes('_')) {
                document.getElementById('result').textContent = 'You won!';
                disableInput();
            }

            // Check if the player lost
            if (attempts === 0) {
                document.getElementById('result').textContent = 'You lost!';
                disableInput();
            }

            // Clear the input field
            document.getElementById('guess-input').value = '';
            
            // Play sound based on whether the guess is correct or not
            if (isCorrectGuess(guessInput)) {
                playSound('correct-sound');
            } else {
                playSound('incorrect-sound');
            }
        } else {
            alert('You already guessed this letter. Try a different one.');
        }
    } else {
        alert('Please enter a single letter.');
    }
}

// Function to play the correct or incorrect sound
function playSound(soundId) {
    var audio = document.getElementById(soundId);
    audio.play().then(() => {
        // The audio started playing successfully
    }).catch((error) => {
        // Autoplay was prevented, handle the error
        console.error("Autoplay prevented. Please interact with the page to enable audio.");
    });
}
    


// Function to play the correct guess sound
function playCorrectSound() {
    var audio = document.getElementById('correct-sound');
    audio.play().then(() => {
        // The audio started playing successfully
        // Check if the word is completely guessed
        if (wordGuessed()) {
            // If the word is completely guessed, clear the input field and disable input
            document.getElementById('guess-input').value = '';
            disableInput();
        }
    }).catch((error) => {
        // Autoplay was prevented, handle the error
        console.error("Autoplay prevented. Please interact with the page to enable audio.");
    });
}



// Function to check if the word is completely guessed
function wordGuessed() {
    return !document.getElementById('word-display').textContent.includes('_');
}

// Function to disable input elements
function disableInput() {
    document.getElementById('guess-input').disabled = true;
    document.querySelector('button').disabled = true;
}
