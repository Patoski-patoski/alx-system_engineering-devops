# Client configuration file (w/ Puppet)
file { '/etc/ssh/ssh_config': # Update the path based on your SSH client configuration file path
  ensure  => present,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}
