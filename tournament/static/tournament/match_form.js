$(function() {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = "https://code.jquery.com/jquery-3.6.0.min.js"; // or your local path to jQuery
  script.onload = function() {
    // Here you can use jQuery functions
    $(function() {
      // Get the tournament field
      var tournament = document.getElementById("id_tournament");

      // Get the team and player fields
      var team1 = document.querySelector(".field-team1");
      var team2 = document.querySelector(".field-team2");
      var player1 = document.querySelector(".field-player1");
      var player2 = document.querySelector(".field-player2");
      var player1_points = document.querySelector(".field-player1_points");
      var player2_points = document.querySelector(".field-player2_points");
      var team1_points = document.querySelector(".field-team1_points");
      var team2_points = document.querySelector(".field-team2_points");
    
      // Hide the team and player fields initially
      team1.style.display = 'none';
      team2.style.display = 'none';
      player1.style.display = 'none';
      player2.style.display = 'none';
      player1_points.style.display = 'none';
      player2_points.style.display = 'none';
      team1_points.style.display = 'none';
      team2_points.style.display = 'none';
  
      // Show the appropriate fields when the tournament type is selected
    
      if (tournament){
        tournamentID = tournament.value;
        $.ajax({
          url: '/admin/tournament/get_tournament/' + tournamentID + '/',
          success: function(response) {
            // Parse the response JSON object to retrieve the tournament_type attribute
            // Modify the form elements accordingly
            if (response.tournament_type == 'Team') {
              team1.style.display = 'inline-block';
              team2.style.display = 'inline-block';
              player1.style.display = 'none';
              player2.style.display = 'none';
              player1_points.style.display = 'none';
              player2_points.style.display = 'none';
            } else if (response.tournament_type == 'Individual') {
              team1.style.display = 'none';
              team2.style.display = 'none';
              team1_points.style.display = 'none';
              team2_points.style.display = 'none';
              player1.style.display = 'inline-block';
              player2.style.display = 'inline-block';
            }
          }
        });
      }

      tournament.onchange = function() {
        var tournamentId = this.value;
        $.ajax({
          url: '/admin/tournament/get_tournament/' + tournamentId + '/',
          success: function(response) {
            // Parse the response JSON object to retrieve the tournament_type attribute
            // Modify the form elements accordingly
            if (response.tournament_type == 'Team') {
              team1.style.display = 'inline-block';
              team2.style.display = 'inline-block';
              player1.style.display = 'none';
              player2.style.display = 'none';
              player1_points.style.display = 'none';
              player2_points.style.display = 'none';
            } else if (response.tournament_type == 'Individual') {
              team1.style.display = 'none';
              team2.style.display = 'none';
              team1_points.style.display = 'none';
              team2_points.style.display = 'none';
              player1.style.display = 'inline-block';
              player2.style.display = 'inline-block';
            }
          }
        });
      }

      
    });
  };
  document.getElementsByTagName("head")[0].appendChild(script);
});