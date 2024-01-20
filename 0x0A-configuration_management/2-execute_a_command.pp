# Puppet Exec Resource to Kill a Process
exec { 'killmenow':
  command => 'pkill killmenow',
}
