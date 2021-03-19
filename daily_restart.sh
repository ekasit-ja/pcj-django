/bin/systemctl restart nginx.service
/bin/systemctl restart uwsgi.service
D=`date`
echo daily_restart is executed at --- $D
