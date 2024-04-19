# Automate the task of creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
#   ** The value of the custom HTTP header must be the hostname of the server 
#      Nginx is running on
# Write 2-puppet_custom_http_response_header.pp so that it configures a brand
# new Ubuntu machine to the requirements asked in this task

# Install nginx on your server
exec {'update and install nginx':
  command => 'sudo apt install -y nginx ; sudo apt -y update',
  path    => '/usr/bin',
  onlyif  => 'sudo /usr/bin/test ! -f /etc/nginx',
}

# Setting up document Root Directories and Creating sample Pages
file {'/var/www/html/index.html':
  ensure  => 'file',
  mode    => '0644',
  content => '
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Patoski Tech</h1>
            <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Illo distinctio deleniti iure vel delectus, officiis similique reiciendis nemo voluptate amet, hic quam autem repellendus. Architecto, iusto vero. Quod enim sed hic!</p>
            <ul>
                <li>Python</li>
                <li>C</li>
                <li>JavaScript</li>
            </ul>
</body>
</html>',
}

# Creating 404 page
file {'/var/www/html/44.html':
  ensure  => 'file',
  mode    => '0644',
  content => "Ceci n'est pas une page\n",
}

#  Create a sym link
exec {'Create a symbolic link':
  command => 'sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled',
  path    => '/usr/bin',
  onlyif  => 'sudo /usr/bin/test ! -f /etc/nginx/sites-enabled/default',
}

# Creating a Server Block
file {'Create a server block':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
#  backup  => 'default_backup',
  content =>
  "server {
                listen 80;
                listen [::]:80;
                root /var/www/html;
                index index.html;

                location /redirect_me {
                        return 301 https://github.com/patoski-patoski;
                }

                add_header X-Served-By \$HOSTNAME;
                error_page 404 /404.html;
                location = /404.html { 
                        internal;
                }
                location / {
                        try_files \$uri \$uri/ =404;
                }
        }",
}
  
  
# Restart nginx
exec {'Restart nginx':
  command => 'sudo service nginx restart',
  path => '/usr/bin',
}
