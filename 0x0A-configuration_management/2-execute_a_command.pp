# a manifest that kills a process named killmenow.

exec { 'kill a process':
  command => 'pkill -f killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
  onlyif  => 'pkill -f killmenow',
}
