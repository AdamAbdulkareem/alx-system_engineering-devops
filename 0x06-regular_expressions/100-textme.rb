#!/usr/bin/env ruby
puts ARGV[0].scan(/Google|\+?\d{11}|\W\d:\d:\W\d\W\W?\d:\W\d/).join(',')
