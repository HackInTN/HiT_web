<?php
session_start();
require(dirname(__FILE__).'/MyBdd.php');

if($_SESSION["user"]==null){
	header('Location: index.php');
}
$bdd = MyBdd::Instance();

if(!empty($_GET["idMessage"])){
	$reponse = $bdd->query("SELECT * FROM message where id=".$_GET["idMessage"]);

}else{
	$reponse = $bdd->query("SELECT * FROM message");	
}


?>





<html>
	<head>
		<title><?php echo $title; ?></title>
	</head>
	<body>
		<h1 style="text-align:center">Messages page</h1>
		<img src="assets/img/meme<?php echo $nb; ?>.jpg" width="300" height="300" style="float:left"/>
		<div style="float:right; text-align:right;">
			<label>Welcome <?php echo $_SESSION["user"]["login"]; ?></label></br>
			<a href="./index.php?logout=1">Logout</a>
		</div>

		<div style="width:700px; margin-left:350px;">
			<?php if(!empty($_GET["idMessage"])){ ?>
			<p align="center">
				<a href="message.php">Go back</a><br>
			</p>
			<?php } ?>
			<?php while ($donnees = $reponse->fetch()){ ?>
				<div style="border-bottom:solid black 1px;margin-top:70px;">
					<?php
						$id=$donnees["idUser"];
						$reponse2 = $bdd->query("SELECT * FROM user WHERE id='$id'");
						$donnees2 = $reponse2->fetch();
					?>
					<label style="font-weight:bold;"><?php echo $donnees2["prenom"]." ".$donnees2["nom"];?></label>
					<label><?php echo $donnees["date"];?></label>
					<a href="message.php?idMessage=<?php echo $donnees["id"];?>">View only this message</a>
					<pre><?php echo $donnees["message"];?></pre>

					<?php
						$reponse2 = $bdd->query("SELECT * FROM fichier WHERE idMessage='".$donnees["id"]."'");
						$donnees2 = $reponse2->fetch();
						if($donnees2){
							$path=$donnees2["path"];
							$name=$donnees2["nom"];
					?>
						Attachment : <a href="./img.php?img=<?php echo $path; ?>" ><?php echo $name ; ?></a>
					<?php } ?>
				</div>

			<?php } ?>
		</div>
	</body>
</html>