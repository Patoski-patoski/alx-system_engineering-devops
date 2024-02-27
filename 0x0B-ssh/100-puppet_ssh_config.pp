# using Puppet to make changes to our configuration file so that you can 
# connect to a server without typing a password.

file { ' /etc/ssh/ssh_config ':
	ensure => file,
	owner => 'root',
	group => 'root',
	mode => '0644',
}

# Disable Password authentication

file_line { 'Turn of passwd auth':
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
	match => '^#?PasswordAuthentication.*',
	ensure => present,
}

# Declare Identity file

file_line = { 'Declare identity file':
	path => '/etc/ssh/shh_config',
	line => 'IdentityFile ~/.ssh/school',
	match => '^#IdentutyFile.*',
	ensure => present,
}
