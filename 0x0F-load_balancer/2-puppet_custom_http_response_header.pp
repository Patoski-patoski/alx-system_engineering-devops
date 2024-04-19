# Define class to install and configure nginx
class web_server {
    package { 'nginx':
        ensure  => installed,
        require => Apt::Update,
    }

    file { '/var/www/html/index.html':
        ensure  => present,
        content => 'Hello World!',
        owner   => 'www-data',
        group   => 'www-data',
        mode    => '0644',
        require => Package['nginx'],
    }

    file { '/etc/nginx/sites-available/default':
        ensure  => present,
        content => template('web_server/nginx_default.erb'),
        require => Package['nginx'],
        notify  => Service['nginx'],
    }

    file { '/etc/nginx/sites-enabled/default':
        ensure  => link,
        target  => '/etc/nginx/sites-available/default',
        require => File['/etc/nginx/sites-available/default'],
        notify  => Service['nginx'],
    }

    service { 'nginx':
        ensure    => running,
        enable    => true,
        hasrestart => true,
        require   => [Package['nginx'], File['/etc/nginx/sites-available/default']],
    }
}

# Define template for nginx default site configuration
# This template will be used to generate the nginx configuration file
# /etc/nginx/sites-available/default
# You need to create a file named nginx_default.erb in your Puppet module's templates directory
# with the following content:
#
# server {
#     listen 80;
#     listen [::]:80;
#     root /var/www/html;
#     index index.html;
#     location / {
#         try_files $uri $uri/ =404;
#     }
#     add_header X-Served-By 305199-web-01;
# }
