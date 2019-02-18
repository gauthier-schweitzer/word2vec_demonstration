$(function(){
	// Traitement du click sur le form 1
	$('#mybutton1').click(function(){
		$.ajax({
			url: '/ajaxhandlerForm1',
			data: $('#wordsform1').serialize(),
			type: 'POST',
			success: function(response){
				// Affichage du résultat de la requête
				$("#result1").text(response["result1"]);
			},
			error: function(error){
				// Affichage de l'erreur
				console.log("error");
			}

		});
	});

	// Traitement du click sur le form 2
	$('#mybutton2').click(function(){
		$.ajax({
			url: '/ajaxhandlerForm2',
			data: $('#wordsform2').serialize(),
			type: 'POST',
			success: function(response){
				// Affichage du résultat de la requête
				$("#result2").text(response["result2"]);
			},
			error: function(error){
				// Affichage de l'erreur
				console.log("error");
			}
		});
	});



});
