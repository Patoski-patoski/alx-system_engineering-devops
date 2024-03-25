# Using Puppet, install flask from pip3

package { 'flask':
 provider => 'pip3',
 ensure   => '2.1.1',
}

package { 'werkzeug':
  provider => 'pip3',
  ensure   => '2.1.0',
}
