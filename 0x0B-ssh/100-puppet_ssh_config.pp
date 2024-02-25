# 100-puppet_ssh_config.pp

# Ensure SSH client configuration
file_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#?PasswordAuthentication',
}

file_line { 'Declare identity file':
  path  => '/home/your_username/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^#?(\s*)IdentityFile',
}

