<?php

final class MyBdd
{
   


    public static function Instance(){
        static $bdd = null;
    	
        if ($bdd === null) {
            try{
			    $bdd = new PDO('mysql:host=127.0.0.1;dbname=sql_app;charset=utf8', 'hackintn', '');
			}catch (Exception $e){
			        die('Erreur : ' . $e->getMessage());
			}
        }
        return $bdd;
    }

    
    private function __construct(){

    }
}


$title = "Epic songs HackInTN";
$nb = rand ( 1 , 7 );

if(isset($_SESSION["user"]) && isset($_SESSION["user"]["time"])){
    if($_SESSION["user"]["time"]+(10*15) < time()){
        header('Location: trolololo.php'); 
        return;
    }
}
