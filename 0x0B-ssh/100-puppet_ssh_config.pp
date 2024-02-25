# 100-puppet_ssh_config.pp

# Ensure SSH client configuration
file_line { 'Turn off passwd auth':
  ensure => 'present',
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/home/your_username/.ssh/config',
  line   => '    IdentityFile ~/.ssh/school',
}

