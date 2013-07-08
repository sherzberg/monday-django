Exec['apt_update'] -> Package <| |>

exec {'apt_update':
  command => '/usr/bin/apt-get update',
}

package {'python-deps':
  name => ['python-pip'],
  ensure => present,
}

package {'django-deps':
  name => ['django', 'django-debug-toolbar', 'djangorestframework'],
  ensure => present,
  provider => pip,
  require => Package['python-deps'],
}
