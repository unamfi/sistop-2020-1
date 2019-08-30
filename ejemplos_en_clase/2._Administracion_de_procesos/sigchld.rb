#!/usr/bin/ruby
# coding: utf-8

# Si comentan esta sección (el manejador de señales para SIGCHLD)
# verán cómo los procesos derivados se mantienen como zombies hasta
# que termina el padre.
Signal.trap('CHLD') do
  regresado = Process.wait
  puts "Soy %d. Atrapé la señal CHLD de %d. Ámonos." % [$$, regresado]
  case regresado
  when @pid_hijo
    puts "¡Miren! Era el hijo 1"
  when @pid_hijo2
    puts "¡Miren! Era el hijo 2"
  end
end

mi_pid = $$
@pid_hijo = fork()
@pid_hijo2 = fork() if @pid_hijo

if @pid_hijo and @pid_hijo2
  # Somos el proceso padre
  puts "El proceso padre es %d. Los procesos hijos son %d y %d." %
       [$$, @pid_hijo, @pid_hijo2]
elsif @pid_hijo.nil?
  # Hijo 1
  sleep(5*rand)
  puts "El hijo 1 ya se fue"
  exit(0)
elsif @pid_hijo2.nil?
  # Hijo 2
  sleep(5*rand)
  puts "El hijo 2 ya se fue"
  exit(0)
end

sleep(5)
puts "El padre también se va"
