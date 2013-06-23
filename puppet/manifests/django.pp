Exec['apt_update'] -> Package <| |>

exec {'apt_update':
  command => '/usr/bin/apt-get update',
}

package {'django-deps':
  name => ['python-pip'],
  ensure => present,
}

