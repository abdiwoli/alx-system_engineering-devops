# Puppet Exec Resource to Kill a Process
exec { 'killmenow':
  command => 'pkill -9 -f  killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin']
}
