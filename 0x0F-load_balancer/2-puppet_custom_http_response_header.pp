# Define a class for configuring Nginx with custom HTTP header
class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/conf.d/custom_header.conf':
    ensure  => present,
    content => "server {
                  listen 80 default_server;
                  server_name _;

                  location / {
                      add_header X-Served-By $hostname;
                      # Other configuration directives...
                  }
                }",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

# Apply the class to configure Nginx with custom header
include nginx_custom_header
