# install flask using puppet
exec { 'install_flask_2.1.0':
    command => '/usr/bin/pip3 install Flask==2.1.0',
    path    => ['/bin', '/usr/bin'],
    unless  => '/usr/bin/pip3 show Flask | grep "Version == 2.1.0"',
}

