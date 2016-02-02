<?php
session_start();
require(dirname(__FILE__).'/MyBdd.php');

$bdd = MyBdd::Instance();

if(!empty($_GET["logout"])){
	session_unset();
}



$fail=false;
$doublefail=false;
$doublefailhtml = "<!-- admin/4DM1N -->";
if (!empty($_POST["username"]) && !empty($_POST["password"])) {
	$u = $_POST["username"];
	$pass = $_POST["password"];
	if ($u==="admin" && $pass==="4DM1N"){
		$doublefail=true;
		$doublefailhtml = "<!-- Et non dommage, le login/mot de passe n'est pas dans le code source :P -->";
		$doublefailhtml .= "<img src=\"assets/img/fail2.png\"/><br>";
	}

	$reponse = $bdd->query("SELECT * FROM user where login='$u' and password='$pass'");
	
	if($reponse){
		$donnees = $reponse->fetch();
		if($donnees){
			
			$user["id"] = $donnees["id"];
			$user["login"] = $donnees["login"];
			$user["email"] = $donnees["email"];
			$user["nom"] = $donnees["nom"];
			$user["prenom"] = $donnees["prenom"];
			$user["password"] = $donnees["password"];
			$user["isAdmin"] = $donnees["isAdmin"];
			$user["time"] = time();
			$_SESSION["user"] = $user;

			//var_dump($user);

			header('Location: message.php'); 
		}else{
			$_SESSION["user"]=null;
			
			$fail=true;
		}
	}else{
		$_SESSION["user"]=null;
		
		$fail=true;
	}

}

?>
<html>
	<head>
		<title><?php echo $title; ?></title>
	</head>
	<body>


		
		<div style="width:500px; margin:auto;">
			<?php echo $doublefailhtml; ?>
			
			<h1>Login</h1>
			<?php if($fail) echo "Login fail"; ?>
			<form method="POST">
				<label for="username">Login* : </label><input type="text" id="username" name="username" /></br>
				<label for="password">Password* : </label><input type="password" id="password" name="password" /></br>
				<button type="submit">Login</button><button type="cancel">Cancel</button>
			</form>
			<?php if($fail && !$doublefail && false){ ?>
				<img src="assets/img/bsod.jpg"/>
			<?php }else{ ?>
				<img src="assets/img/tortue.png"/>
				<!-- Oui oui, j'aime les tortues :D -->
			<?php } ?>
		</div>
	</body>
</head>
