<?php
   # get data and forward it to two (or more) web servers
   # @rahard

   # get the original query
   $query = $_SERVER['QUERY_STRING'];

   # send the query to host1 using curl
   $host1 = 'localhost:8008';
   $fullurl= "$host1/weather/update.php?$query";
   $ch = curl_init();
   curl_setopt($ch, CURLOPT_URL, $fullurl);
   $output = curl_exec($ch);
   curl_close($ch);

   # send the query to host2 using curl 
   $host2 = 'localhost:8008';
   $fullurl= "$host2/weather/update.php?$query";
   $ch = curl_init();
   curl_setopt($ch, CURLOPT_URL, $fullurl);
   $output = curl_exec($ch);
   curl_close($ch);

?>
