# Using Puppet to create a file in /tmp

file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  path    => '/tmp/school',
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n",
}
