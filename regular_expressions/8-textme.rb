#!/bin/usr/env ruby
log_file_path = "logfile.txt"

from = /\[(.*?)\]/
to = /\[(.*?)\]/
flags = /\[(.*?)\]/

File.open(logfile.txt, "r") do |file|
  file.each_line do |line|
    line.match(from) do |m|
      from = m[1]
      puts "Sender: #{from}"
    end

    line.match(to) do |m|
      to = m[1]
      puts "Receiver: #{to}"
    end

    line.match(flags) do |m|
      flags = m[1]
      puts "Flags: #{flags}"
    end
  end
end

