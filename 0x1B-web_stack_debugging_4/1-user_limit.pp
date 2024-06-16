# Change the OS configuration so that it is possible to login with the
#  holberton user and open a file without any error message.
file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
