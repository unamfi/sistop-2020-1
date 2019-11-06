defmodule Procmem do
  @moduledoc """
  Procmem
  ---

  Asigna los procesos en memoria.

  Este utiliza el primer ajuste.
  """


  @doc """
  Inicializa los procesoe en memoria, si no hay argumento en --procesos,
  se generan aproximadamente 30 espacios de memoria con posibles procesos
  """
  def proc(cadena) do
    if cadena[:procesos] do
      cad = String.to_charlist(cadena[:procesos])
      menu_interactivo(cad)
    else
      cad = gen_proc_ale([])
      menu_interactivo(to_charlist(to_string(cad)))
    end
  end

  @doc """
  Es el menu del programa
  """
  def menu_interactivo(cad) do
    IO.puts("\nAsignación:\n#{cad}")
    opt = String.trim(IO.gets('Asignar o Liberar [a/l]: '))
    cond do
      opt in ["l", "L"] ->
	
	libe = String.trim(IO.gets("Proceso a liberar: "))
	Enum.map(cad, fn (i) -> if to_charlist(<<i>>)==to_charlist(libe) do 45
	      else i
	end end)
	|>menu_interactivo()
		 
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

  @doc """
  # Primer Ajuste
  
  Busca el primer espació donde el proceso entrante pueda caber,
  Si no cabe, se intenta una compactación de procesos entre la 
  memoria.
  """
  def asignar_primero(cad, proc_nom, tam, flag \\ :true) do
    if flag do
      cad = to_string(cad)
      proc_nom = to_string(List.duplicate(proc_nom, tam))
      {_, exp} = Regex.compile(to_string(List.duplicate("-", tam)))
      resp = to_charlist(Regex.replace(exp, to_string(cad),
	    to_string(proc_nom), global: false))

      cond do
	cad == to_string(resp) ->
	  IO.puts("*Compactación Requerida*")
	  asn_new = comprimir(cad)
	  if to_string(asn_new) == cad do
	    IO.puts("\n\e[41mNo hay espacio para el proceso\e[0m\n")
	    {_, exp} = Regex.compile(to_string(List.duplicate("-", tam)))
	    to_charlist(Regex.replace(exp, to_string(cad),
		  to_string(proc_nom), global: false))
	  end
	  IO.puts("Asignando a #{proc_nom}")
	  to_charlist(Regex.replace(exp, to_string(asn_new),
		to_string(proc_nom), global: false))
	  :true -> resp
	  
      end
    end

    
  end

  @doc """
  Un buen bubblesort para mover los espacios de memoria
  """
  def comprimir(cad)do
    asig_new = cad
    |> to_charlist()
    |> bubblesort()
    IO.puts("Nueva situación:\n#{asig_new}")
    asig_new
  end


  defp bubblesort([]), do: []
  
  defp bubblesort(lista) do
    cond do
      swap_itr(lista) == lista -> lista
      :true -> bubblesort(swap_itr(lista))
    end
  end

  defp swap_itr([x | []]), do: [x]

  defp swap_itr([f | [s|r]]) do
    cond do
      f != 45 -> [f | swap_itr([s | r])]
      :true -> [s|swap_itr([f|r])]
    end
  end
  
  defp sel_new_proc(list_proc, proc) do
    cond do
      proc in list_proc -> sel_new_proc(list_proc, proc + 1)
      :true -> proc
    end
  end

  @doc """
  Genera aproximadamente 30 procesos aleatorios, ya sea libres o no
  """
  def gen_proc_ale(list, cont \\ 1) do
    num_al = Enum.random(1..6)
    unless cont > 31 do
      if 1 === Enum.random(0..1) do
	gen_proc_ale([List.duplicate(45, num_al)|list], cont+num_al)
      else
	{char, _} = List.pop_at('abcdefghigklmnopqrstuvwxyz', Enum.random(0..26))       
	li = List.duplicate(char, num_al)
	gen_proc_ale([li | list], cont + num_al)
      end
    else
      list
    end
  end

end
