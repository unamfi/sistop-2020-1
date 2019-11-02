defmodule Asigmem do
  @moduledoc """
  Documentation for Asigmem.
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

  defp parse_args(args) do
    OptionParser.parse(args,
      switches: [
	help: :boolean,
	procesos: :string,
	primer: :boolean,
	mejor: :boolean,
	peor: :boolean
      ],
      aliases: [
	h: :help,
	p: :procesos,
	a: :ajuste,
      ]
    )
   
  end

  defp process(options) do
    IO.inspect options

    case options do
      {[help: :true], _, _} -> IO.puts help_cli()
      {lista, _, _} -> Procmem.proc(lista)
      {[],[],[]} -> noargs()     

      
    end
  end

  defp help_cli() do
    """
    
    asigmem [ARGUMENTOS]

    --help, -h\t Este mensaje
    --procesos, -p\t Define los 30 procesos que el usuario quiera
    --ajuste, -a\t Selecione 'peor', 'mejor' o 'primer' ajuste
    """
  end

end
