# pupet script
exec { 'Change OS configuration for holberton user':
  command => '/bin/su -c "echo -e \'*-nofile 1024\' >> /etc/security/limits.conf" - root',
}
