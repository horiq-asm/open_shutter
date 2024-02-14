#!/bin/bash
echo "Content-type:text/html"
echo ""

echo "<link rel=\"stylesheet\" type=\"text/css\" href=\"/rq/apple-watch.css\">"
echo "<p id=\"p1\">"
echo "Complete<BR>"
echo "<BR>from "
echo $REMOTE_ADDR
echo $REMOTE_ADDR >/var/www/html/rq/mk1.txt
echo "<BR>"
echo $QUERY_STRING >> /var/www/html/rq/mk1.txt
CMM=(${QUERY_STRING//&/ })
if [ "$CMM" = "k1=OPEN" ]; then
   command="python /usr/lib/cgi-bin/rq/mk1-up.py"
else
   command="python /usr/lib/cgi-bin/rq/mk1-up.py"
fi
   eval $command
echo "</p>"
