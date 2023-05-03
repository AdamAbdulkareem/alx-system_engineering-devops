#!/usr/bin/env ruby
puts ARGV[0].scan(/Google|\W\d{11}|\W\d:\d:\W\d\W\W?\d:\W\d/).join(',')
