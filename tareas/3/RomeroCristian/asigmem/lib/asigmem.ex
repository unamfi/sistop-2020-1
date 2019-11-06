defmodule Asigmem do
  @moduledoc """
  Asignación de Memoria
  ---

  Este modulo es el menu que recibe las instrucciónes
  del usuario
  """

  @doc """
  Recibe los argumentos del emulador de terminal
  """
  def main(args) do
    args
    |> parse_args
    |> process
  end

  defp noargs() do
    mensaje =
    """
    \e[0;31mError\e[0m: no se ha pasado ningun argumento
    
    \t--help, -h\tPara ayuda
    """
    IO.puts mensaje
    System.halt(1)
  end

  @doc """
  Analiza los argumentos
  """
  def parse_args(args) do
    OptionParser.parse(args,
      switches: [
	help: :boolean,
	procesos: :string
      ],
      aliases: [
	h: :help,
	p: :procesos
      ]
    )
   
  end

  @doc """
  Inicia el programa analizando ya los argumentos
  """
  def process(options) do
    case options do
      {[help: :true], _, _} -> IO.puts help_cli()
      {[],[],[]} -> Procmem.proc([])    
      {lista, _, _} -> Procmem.proc(lista)
      :true -> noargs()
    end
  end

  defp help_cli() do
    """
    
    asigmem [ARGUMENTOS]

    --help, -h\t Este mensaje
    --procesos, -p\t Define los procesos que el usuario quiera, '-' es memoria libre
    \tEjemplo ./asigmem -p aa--b-ccddeeeefff------
    """
  end

end
