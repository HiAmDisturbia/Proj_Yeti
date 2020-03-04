function myFunction() {
  /*Le retour du regex, mais cette fois on est sur javascript.
  Ensuite on sélectionne les valeurs des deux div (bouton) du fichier html.*/
  var exp_regex = new RegExp(/([0-9]+)\/([0-9]+)\/([0-9]+)/, 'i')
  var x = document.getElementsByClassName("bouton-date")[0].value;
  var y = document.getElementsByClassName("bouton-date")[1].value;

  /*Permet de voir les valeurs obtenues, ainsi que les résultats des tests*/
  console.log(x);
  console.log(y);
  console.log(exp_regex.test(x));
  console.log(exp_regex.test(y));

  /*Si les deux tests sont réussis, ie: test1 == test2*/
  if (exp_regex.test(x) && exp_regex.test(y))
  {
    return (x, y);
  } else {
    alert("Format de date saisie invalide");
    x = "None";
    y = "None";
    return (x, y);
  };
}
// click sur le bouton sauver
var x= $(function (event){
  $('#sauve').click(function(){
    $.getJSON('/',function(data){
    });
    test = document.getElementById("sauve");
    test.value = "date_stockée";
  });
});
var bout = document.getElementById("sauve");
bout.addEventListener("submit",x);
