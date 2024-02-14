#!/bin/bash
echo "Content-type:text/html"
echo ""

echo "<html>"
echo "<head>"
echo "<meta charset=\"utf-8\"/>"
echo "<link rel=\"stylesheet\" type=\"text/css\" href=\"/rq/apple-watch.css\">"
echo "</head>"
echo "<body>"
echo "<p id=\"p1\">"
#ip n | grep 00:1e:5e:02:6b:68 | cut -f 1 -d " " >RED_DOOR
if [ `/usr/lib/cgi-bin/k1-status.py | grep -c 1800131` = 1 ];  then
   echo "<span style=\"color:#FF0000;\">開錠中</span>"
else
   echo "<span style=\"color:#00FF00;\">施錠中</span>"
fi
echo "</p>"
echo "</body>"
echo "</html>"
