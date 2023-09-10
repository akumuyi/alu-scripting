#!/usr/bin/env ruby
# textme.rb

# Check if the log file path is provided as a command line argument
if ARGV.length == 0
  puts "Usage: ./textme.rb <log_file_path>"
  exit
end

log_file_path = ARGV[0]

# Check if the log file exists
unless File.exist?(log_file_path)
  puts "Log file not found: #{log_file_path}"
  exit
end

# Read and process the log file
File.open(log_file_path, "r") do |file|
  file.each_line do |log_entry|
    sender = log_entry.match(/\[from:(.*?)\]/)&.captures&.first
    receiver = log_entry.match(/\[to:(.*?)\]/)&.captures&.first
    flags = log_entry.match(/\[flags:(.*?)\]/)&.captures&.first

    if sender && receiver && flags
      puts "#{sender},#{receiver},#{flags}"
    else
      puts "Invalid log entry format in line: #{log_entry.strip}"
    end
  end
end
