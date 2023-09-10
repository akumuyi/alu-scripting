#!/usr/bin/env ruby
puts File.read(ARGV[0]).scan(/\[from:(.*?)\].*?\[to:(.*?)\].*?\[flags:(.*?)\]/).map { |sender, receiver, flags| "#{sender},#{receiver},#{flags}" }
