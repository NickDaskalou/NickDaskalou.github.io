﻿<html>
<head>
<meta name="viewport" content="width=device-width" />
<title>Music Controller</title>
</head>
	<body>
		<form method="get" action="index.php">
			<input type="submit" value="PLAY" name="first" style="width: 100%; height: 50%; background-color:aquamarine; font-size: 60">
			<input type="submit" value="STOP" name="second" style="width: 100%; height: 50%; background-color:tomato; font-size: 60">
		</form>
	<?php
		if(isset($_GET['first'])){
			exec(" sudo  python /var/www/html/play.py > /dev/null &");
		}
		if(isset($_GET['second'])){
			exec(" sudo python /var/www/html/stop.py > /dev/null &");
		}
	?>
	</body>
</html>
