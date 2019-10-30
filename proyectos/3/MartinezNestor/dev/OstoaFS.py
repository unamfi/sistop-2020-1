"""docstring"""
import optparse
from fslib.clim import CommandManager

def main():
	"""docstring"""
	usage = "usage: %prog [options] arg1"

	parser = optparse.OptionParser(usage=usage)
	parser.add_option("-d", "--defrag", action="callback", callback=filter, help="defragments FiUnamFS")
	parser.add_option("-i", "--copyinside", action="callback", callback=filter, type="string", dest="file_to_copy", help="copy a file from your current dir to FiUnamFS root dir", metavar="<file_to_copy>")
	parser.add_option("-l", "-s", "--list", action="callback", callback=filter,help="lists files inside FiUnamFS root dir")
	parser.add_option("-o", "--copyoutside", action="callback", callback=filter, type="string", dest="file_to_copy", help="copy a file from FiUnamFS root dir to cpo_files dir in your current dir", metavar="<file_to_copy>")
	parser.add_option("-t", "--track", action="callback", callback=filter, help="tracks files inside FiUnamFS root dir and lists concrete system info about each dir entry")
	parser.add_option("-r", "--remove", action="callback", callback=filter, type="string", dest="file_to_remove", help="removes a file from FiUnamFS", metavar="<file_to_remove>")
	
	parser.parse_args()

def filter(option, opt, value, parser):
	climanager = CommandManager()

	if opt in ('-l','--list'):
		climanager.ls_()
	elif opt in ('-i','--copyinside'):
		climanager.cpi(value)
	elif opt in ('-o','--copyoutside'):
		climanager.cpo(value)
	elif opt in ('-r','--remove'):
		climanager.rm(value)
	elif opt in ('-d','--defrag'):
		climanager.defrag()
	elif opt in ('-t','--track'):
		climanager.track()


if __name__ == '__main__':
	main()
