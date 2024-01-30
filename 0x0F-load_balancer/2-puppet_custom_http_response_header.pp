# 2-puppet_custom_http_response_header.pp

# Ensure Nginx is installed and the service is running
class { 'nginx':
  ensure => 'installed',
  enable => true,
  status => 'running',
}

# Define a custom fact to get the hostname
$server_hostname = $facts['hostname']

# Define the Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

# Define an ERB template for the Nginx configuration file
# This template sets up the custom HTTP response header
file { '/etc/nginx/sites-available/default.erb':
  ensure  => file,
  content => '# nginx default configuration file (template)',
}

# Define the Nginx service
service { 'nginx':
  ensure => 'running',
}
