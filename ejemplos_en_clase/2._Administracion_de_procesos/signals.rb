#!/usr/bin/ruby
# coding: utf-8

Signal.trap('WINCH') do
  puts "Cambio de dimensiones"
end

Signal.trap('TERM') do
  puts "Soy más fuerte de lo que crees"
end

Signal.trap('INT') do
  puts "No puedes matarme, lo siento"
end

sleep(100)
