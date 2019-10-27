import sys, getopt

def main(argv): 	
	try:
		opts, args = getopt.getopt(argv,"h", ["help"])
	except getopt.GetoptError:
		print('OstoaFS.py: not a valid option\nTry \'python3 OstoaFS.py -h for help\'')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ('-h',"--help"):
			print("OstoaFS:\n\n\t \033[1m -ls (--list): \033[0m \tlists all the files inside the current FiUnamFs.\n\n\t \033[1m -cpi (--copyinside) <file_to_copy>: \033[0m \tcopy a file in you current dir to FiUnamFS. \n\n\t \033[1m -cpo (--copyoutside) <file_to_copy>: \033[0m\tcopy a file from FiUnamFS to your current dir.\n\n\t \033[1m -rem (--remove) <file_to_remove>: \033[0m \tremoves a file from FiUnamFs. \n\n\t \033[1m -def (--defrag):\033[0m \tdefragments FiUnamFs.")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg 
		elif opt in ("-o", "--ofile"):
			outputfile = arg 


if __name__ == '__main__':
	main(sys.argv[1:])
