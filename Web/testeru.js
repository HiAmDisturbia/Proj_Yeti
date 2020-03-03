//Ce code a été réalisé dans le but de créer un outil d'analyse du serveur Yéti. Il est utilisé dans le code html, et génère deux fonctions.
//La première fonction vérifie que l'utilisateur saisie correctement le format de date.
//La deuxième, mise dans une variable, permet à l'utilisateur de rester sur la même page, après avoir cliqué sur la balise, qui a
//comme paramètre: "id='sauve'".

function myFunction() {
  //Sélection des valeurs des deux input (type="submit") de homepage.html.
  var exp_regex = new RegExp(/([0-9]+)\/([0-9]+)\/([0-9]+)/, 'i')
  var x = document.getElementsByClassName("bouton-date")[0].value;
  var y = document.getElementsByClassName("bouton-date")[1].value;

  //Permet de voir les valeurs obtenues, ainsi que les résultats des tests
  console.log(x);
  console.log(y);
  console.log(exp_regex.test(x));
  console.log(exp_regex.test(y));

  //Envoie un message d'alerte lorsque l'utilisateur ne saisit pas les dates au format correct.
  if (exp_regex.test(x) && exp_regex.test(y))
  {
  } else {
    alert("Format de date saisie invalide");
  };
}
// Permet d'indiquer l'action à faire, lorsqu'on clique sur le input type="submit" name=""
var x = $(function (event){
  $('#sauve').click(function(){
    $.getJSON('/',function(data){
    });
    test = document.getElementById("sauve");
    test.value = "Date stockée";
  });
});

var bout = document.getElementById("sauve");
bout.addEventListener("submit",x);
