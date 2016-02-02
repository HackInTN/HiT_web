<?php

session_start();
require(dirname(__FILE__).'/MyBdd.php');

$bdd = MyBdd::Instance();

if( empty($_GET["img"]) ){
	$file_existe=false;
	//echo "Vous n'avez pas le droit.";
	//echo "<a href=\"message.php\">Revenir en arrière</a>";
}else{
	$admin = $_SESSION["user"]["isAdmin"];
	$ok=true;
	$file_existe = file_exists($_GET["img"]);
	if( $file_existe && !$admin && substr($_GET["img"], 0, 4)!== "user" ){
		$ok=false;
	} 
}


?>


<html>
	<head>
		<title><?php echo $title; ?></title>
	</head>
	<body>
		<h1 style="text-align:center">Image viewer</h1>
		<?php if($ok && $file_existe){ ?>
			<p align="center">
				<a href="message.php">Go back</a><br>
				<img src="<?php echo $_GET["img"]; ?>" width="300" height="300"/>
			</p>
		<?php }elseif(!$file_existe){ ?>
			<label>File doesn't exists.</label>
		<?php }else{ ?>
			<label>You don't have the right to access to this image.</label>
		<?php } ?>
	</body>
</html>