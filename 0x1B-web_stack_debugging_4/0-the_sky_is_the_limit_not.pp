# trying to debug the server
exec { 'Adjust Nginx config':
  command => '/usr/bin/env sed -i s/15/1000/ /etc/default/nginx',
}

exec { 'Restart Nginx':
  command     => '/usr/bin/env service nginx restart',
  refreshonly => true,
  subscribe   => Exec['Adjust Nginx config'],
}