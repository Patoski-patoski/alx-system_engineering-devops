# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) using curl, 
# it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”

# Update and Install the nginx server
exec {'update and install nginx':
  command => 'sudo apt -y update ; sudo apt install -y nginx',
  path    => '/usr/bin', 
  onlyif  => 'sudo /usr/bin/test ! -f /etc/nginx/',
}

# Setting up document Root Directories and Creating sample Pages
file { '/var/www/html/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  mode    => '0755',
  content => 'Hello World!',
}

# Creating the 404 error page
file { '/var/www/html/404.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  mode    => '0755',
  content => "Ceci n'est pas une page\n",
}

# Creating a Server Block
file { 'Create the server block':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  owner   => 'ubuntu',
  backup  => '.my_back',
  content =>
  "server {
		listen 80 default_server;
		listen [::]:80 default_server;
		root /var/www/html;
		index index.html;
		
		location = /patoski {
			return 301 https://github.com/patoski-patoski;
			error_page 404 /404.html;
		}
		location / {
			try_files \$uri \$uri/ =404;
		}
	}",
}

# Create a sym link
exec { 'Creating a symbolic link':
  command  => 'sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled',
  path     => 'usr/bin',
  onlyif   => '/usr/bin/test ! -f /etc/nginx/sites-enabled/default',
}
