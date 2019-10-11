#!/usr/bin/ruby
# coding: utf-8
# Parametros: 0 - Nombre del archivo
#             1 - Ancho del registro
#             2 - Columna a mostrar
#             3 - Periodo

filename = ARGV[0]
width = ARGV[1].to_i
column = ARGV[2].to_i
period = ARGV[3].to_i

fh = open(filename, 'r')
iter = 0
while true
  fh.seek(iter + column)
  char = fh.read(1)
  if char.nil?
    exit 0
  end
  print char
  #  puts "El caracter número #{column} es: «#{char}»"
  iter = iter + (width * period)
end
