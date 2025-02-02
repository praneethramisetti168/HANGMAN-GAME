// // Function to update the leaderboard
// function updateLeaderboard(player, guesses, outcome) {
//     var leaderboardBody = document.getElementById('leaderboardBody');
  
//     // Create a new row
//     var newRow = document.createElement('tr');
  
//     // Add cells with player, guesses, and outcome
//     var playerCell = document.createElement('td');
//     playerCell.textContent = player;
//     newRow.appendChild(playerCell);
  
//     var guessesCell = document.createElement('td');
//     guessesCell.textContent = guesses;
//     newRow.appendChild(guessesCell);
  
//     var outcomeCell = document.createElement('td');
//     outcomeCell.textContent = outcome;
//     newRow.appendChild(outcomeCell);
  
//     // Append the new row to the leaderboard
//     leaderboardBody.appendChild(newRow);
//   }
  
//   // Function to handle the completion of the Hangman game
//   function handleGameCompletion(player, guesses, outcome) {
//     // Update the leaderboard
//     updateLeaderboard(player, guesses, outcome);
//   }

        // Assume this function is called when the game is finished
        function finishGame(player, guesses, result) {
            // Assume there is an API endpoint to update the leaderboard on the server
            // You may need to replace this with your actual API endpoint
            const leaderboardEndpoint = '/update-leaderboard';

            // Make a POST request to update the leaderboard
            fetch(leaderboardEndpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    player: player,
                    guesses: guesses,
                    result: result,
                }),
            })
            .then(response => response.json())
            .then(data => {
                // Assume the data returned contains updated leaderboard information
                // You may need to update the DOM with the new leaderboard data
                updateDashboard(data);
            })
            .catch(error => {
                console.error('Error updating leaderboard:', error);
            });
        }

        // Assume this function updates the dashboard with new leaderboard data
        function updateDashboard(data) {
            // Assuming there is an element with the ID 'leaderboardBody' in the dashboard
            const leaderboardBody = document.getElementById('leaderboardBody');

            // Clear existing leaderboard rows
            leaderboardBody.innerHTML = '';

            // Iterate through the new data and add rows to the leaderboard
            data.forEach(entry => {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${entry.player}</td><td>${entry.guesses}</td><td>${entry.result}</td>`;
                leaderboardBody.appendChild(row);
            });
        }
    
  