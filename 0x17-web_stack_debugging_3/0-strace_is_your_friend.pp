# 0x17-debugging_3

exec { 'Fix_wp-settings.php':
  command => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
  provider => shell,
}
