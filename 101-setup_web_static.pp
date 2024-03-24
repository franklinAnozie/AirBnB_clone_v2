# Prepare web server for deployment

exec {'update apt':
  provider => shell,
  command  => 'sudo apt-get update',
}

-> exec {'install nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
}

-> exec {'start nginx':
  provider => shell,
  command  => 'sudo service nginx start',
}

-> exec {'create data web_static shared':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/shared/',
}

-> exec {'create release test':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test/',
}

-> exec {'add test content':
  provider => shell,
  command  => 'echo "<h1>HI<h1>" > /data/web_static/releases/test/index.html',
}

-> exec {'create symbolic link to current':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
}

-> file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

-> exec {'add bnbn_static path current':
  provider => shell,
  command  => 'sed -i "61i\ \n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tautoindex off;\n\t}" /etc/nginx/sites-available/default',
}

-> exec {'restart nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
