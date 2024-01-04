#!/usr/bin/env ruby

# ruby_script.rb

def match_pattern(input)
  pattern = /\A\d{3}-\d{2}-\d{4}\z/  # Example pattern for a Social Security Number (SSN)

  if input =~ pattern
    puts "The input '#{input}' matches the pattern."
  else
    puts "The input '#{input}' does not match the pattern."
  end
end

# Check if a command-line argument is provided
if ARGV.empty?
  puts "Usage: ruby ruby_script.rb <input>"
else
  # Get the first command-line argument
  user_input = ARGV[0]

  # Call the method to match the pattern
  match_pattern(user_input)
end

