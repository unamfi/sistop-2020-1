defmodule Fiunamfs do
  @moduledoc """
  Documentation for Fiunamfs.
  """

  def main(args) do
    args
    |> analizar_argumento
    |> procesar_argumentos
  end

  defp analizar_argumento(args) do
    OptionParser.parse(args,
      switches: [
	help: :boolean,
	root: :string,
	name_vol: :string,
	create: :boolean],
      aliases: [
	h: :help,
	r: :root,
	n: :name_vol])
  end

  defp procesar_argumentos(opts) do
    IO.inspect opts
    case opts do
      {[help: true],_, _} ->
	IO.puts(print_help())
	System.halt(0)
      _ ->
	IO.puts(print_help_manual())
	System.halt(1)
    end
  end

  defp print_help do
    man_root = "Define el archivo que contiene o "<>
      "contendra el sistema de archivos"
    man_name_vol = "Define la etiqueta del volumen"
    man_create = "Define si se creara nuevo sistema de archivos"
    """
    
    $ fiunamfs [COMMANDOS]

    FiunamFS

    Comandos:
    \t--help, -h\tImprime este manual.
    \t--root, -r\t#{man_root}
    \t--name_vol, -v\t#{man_name_vol}
    \t--create, -c\t#{man_create}

    """
  end

  defp print_help_manual do
    rojo = fn(cadena) ->
      "\e[0;31m#{cadena}\e[0;0m" end
    """
    #{rojo.("Error Fatal")}: Argumentos fallidos
    --help, -h\tImprime la ayuda
    """
  end

  
end
