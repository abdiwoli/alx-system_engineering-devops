#!/usr/bin/env ruby
fr = ARGV[0].scan(/\[from:(.*?)\]/).flatten.join(" ")
fr += "," + ARGV[0].scan(/\[to:(\+\d{8,16})\]/).flatten.join(" ") + ","
puts fr +  ARGV[0].scan(/\[flags:(.*?)\]/).flatten.join(" ")
