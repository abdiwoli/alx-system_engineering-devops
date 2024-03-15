# trying to debug the server
# Puppet script to adjust the maximum number of open files for the holberton user

file_line { 'Increase open file limit for holberton user':
  path    => '/etc/security/limits.conf',
  line    => '*                soft    nofile          1024',
  ensure  => present,
  match   => '^*.*holberton.*nofile',
}

file_line { 'Increase open file limit for holberton user (hard limit)':
  path    => '/etc/security/limits.conf',
  line    => '*                hard    nofile          1024',
  ensure  => present,
  match   => '^*.*holberton.*nofile',
}

file_line { 'Increase open file limit for session':
  path    => '/etc/pam.d/common-session',
  line    => 'session required        pam_limits.so',
  ensure  => present,
  match   => '^session.*pam_limits.so',
}

exec { 'Restart PAM service':
  command     => '/bin/systemctl restart systemd-logind',
  refreshonly => true,
}
