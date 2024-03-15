# Puppet script to adjust the OS configuration for the holberton user

file_line { 'Increase open file limit for holberton user':
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 1024',
  ensure  => present,
}

file_line { 'Include pam_limits module':
  path    => '/etc/pam.d/common-session',
  line    => 'session required pam_limits.so',
  ensure  => present,
}

service { 'restart-login':
  name    => 'systemd-logind',
  ensure  => 'running',
  enable  => true,
  subscribe => File_line['Increase open file limit for holberton user', 'Include pam_limits module'],
}
k