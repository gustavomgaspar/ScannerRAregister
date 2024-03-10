<?php
#db config
$servername = "192.168.1.101"; #charge to your db server ip
$database = "labtest";
$username = "root";
$password = "root_password";


#debug
function console_log($data) {
    $stdout = fopen("php://stdout", "w");
    fwrite($stdout,"\n".$data."\n");
    fclose($stdout);
}

$_POST = json_decode(file_get_contents('php://input'), true);

if (isset($_POST['RA'])){
    date_default_timezone_set("America/Sao_Paulo");
    $conn = mysqli_connect($servername, $username, $password, $database);
    // Check connection
    if (!$conn) {
          die("Connection failed: " . mysqli_connect_error());
    }
 
   
    $dataTime = date("Y-m-d H:i:s");
    $RA = $_POST['RA'];
    console_log($dataTime);
     $sql = "INSERT INTO logalunos (RA, DATA ) VALUES ( '".$RA."','".$dataTime."' )";
    if (mysqli_query($conn, $sql)) {
        echo "New record created successfully";
    } else {
     console_log( "Error: " . $sql . "<br>" . mysqli_error($conn));
    }
    mysqli_close($conn);

    
}

