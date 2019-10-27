import optparse

def main(): 	
	usage = "usage: %prog [options] arg1"

	parser = optparse.OptionParser(usage=usage)
	parser.add_option("-l", "-s", "--list", action="callback", callback=filter,help="lists all the files inside the current FiUnamFs")
	parser.add_option("-i", "--copyinside", action="callback", callback=filter, type="string", dest="file_to_copy", help="copy a file in you current dir to FiUnamFS", metavar="<file_to_copy>")
	parser.add_option("-o", "--copyoutside", action="callback", callback=filter, type="string", dest="file_to_copy", help="copy a file from FiUnamFS to your current dir", metavar="<file_to_copy>")
	parser.add_option("-r", "--remove", action="callback", callback=filter, type="string", dest="file_to_remove", help="removes a file from FiUnamFs", metavar="<file_to_remove>")
	parser.add_option("-d", "--defrag", action="callback", callback=filter, help="defragments FiUnamFs")
	
	(options, args) = parser.parse_args()

def filter(option, opt, value, parser):
	if opt in ('-l','--list'):
		print("List")
	elif opt in ('-i','--copyinside'):
		print("copy inside", value)
	elif opt in ('-o','--copyoutside'):
		print("copy outside", value)
	elif opt in ('-r','--remove'):
		print("remove", value)
	elif opt in ('-d','--defrag'):
		print("defrag")


if __name__ == '__main__':
	main()
