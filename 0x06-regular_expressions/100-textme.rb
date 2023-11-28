#!/usr/bin/env ruby
fr = ARGV[0].scan(/\[from:(\w{4,15})\]/).flatten.join(" ")
fr += " + " + ARGV[0].scan(/\+\d{8,16}/).join(" ") + " "
puts fr +  ARGV[0].scan(/\[flags:(.*?)\]/).flatten.join(" ")



