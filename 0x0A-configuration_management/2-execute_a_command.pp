# This script uses puppet to create a manifest that kills a process named killmenow
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
