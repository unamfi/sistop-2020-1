defmodule Procmem do


  # {[procesos: "ABCD", mejor: true, peor: true, primer: true], [], []}
  def proc(cadena) do
    if cadena[:procesos] do
      cad = String.to_charlist(cadena[:procesos])
      cont = 0
      cont =  conta_esp_libre('----a-')
      menu_interactivo(cad)
    end
  end

  defp menu_interactivo(cad) do
    IO.puts("\nAsignación:\n#{cad}")
    opt = String.trim(IO.gets('Asignar o Liberar [a/l]: '))

    cond do
      opt in ["l", "L"] ->
      
	libe = String.trim(IO.gets("Proceso a liberar: "))
	menu_interactivo(Enum.map(cad, fn (i) ->
	  if to_charlist(<<i>>)==to_charlist(libe) do
	    45 else i
	  end
	end))
      opt in ["a", "A"] ->
	proc_id = <<sel_new_proc(cad, 97)>>
	new_proc_tam = String.to_integer(String.trim(
	    IO.gets("Nuevo Proceso [#{proc_id}] "))) 
	menu_interactivo(asignar_primero(cad, proc_id, new_proc_tam))
      opt in ["q", "Q"] ->
	0
	true -> menu_interactivo(cad)
    end
  end

  defp asignar_primero(cad, proc_nom, tam) do
    cad = to_string(cad)
    proc_nom = to_string(List.duplicate(proc_nom, tam))
    {_, exp} = Regex.compile(to_string(List.duplicate("-", tam)))
    to_charlist(Regex.replace(exp, to_string(cad),
      to_string(proc_nom), global: false))

   
    
  end

  defp sel_new_proc(list_proc, proc \\ 97) do
    cond do
      proc in list_proc -> sel_new_proc(list_proc, proc + 1)
      :true -> proc
    end
  end

  defp conta_esp_libre([head | tail],conta\\0) do
    cond do
      head != ?- -> conta
      :true ->
	conta_esp_libre(tail, conta + 1)
    end
  end

  defp gen_proc_ale() do
    l= for i <- ['a','b','c','d','f','g'] do
      if 1 === Enum.random(0..3) do
	45
      else
	List.duplicate(i, Enum.random(1..5))
      end
    end
    List.to_charlist(l)
  end
  
end
