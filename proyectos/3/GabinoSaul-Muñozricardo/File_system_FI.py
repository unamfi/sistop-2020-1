import os
import subprocess
import time
from datetime import datetime
import math
import getpass



username = getpass.getuser()

file_names = []
file_content_locator = []
file_sizes = []

file_system_name = 'FiUnamFS'
file_system_version = '0.4'
volume_tag = 'FiUnamFS.img' 
cluster_length = '1024'
num_of_clusters_dir = '4'
num_of_clusters_unit = '1440'
'''
El directorio inicia en el cluster 1. 
Es decir, en el byte 1024
'''
init_dir = 1024
info_size = 64

disk_name = 'FiUnamFS.img'
actual_pointer = init_dir

limit_of_files = 64
no_file_name = 'UPS_no_hay_nada'
no_size = '00000000'
no_init_cluster = '00000'
no_date = '00000000000000'


def create_file_system_disk():
	global file_system_name,file_system_version
	global volume_tag,cluster_length,num_of_clusters_dir,num_of_clusters_unit
	global actual_pointer,no_file_name,no_size,no_init_cluster,no_date

	insert_bytes(0,  8,  file_system_name)
	insert_bytes(10, 13, file_system_version)
	insert_bytes(20, 35, volume_tag)
	insert_bytes(40, 45, cluster_length)
	insert_bytes(47, 49, num_of_clusters_dir)
	insert_bytes(52, 60, num_of_clusters_unit)

	for i in range(limit_of_files): #Aquí es 64 por que es el tamaño del directorio 1024 * 4 = 4096 = 64bytes*64
		insert_bytes(actual_pointer + 0,  actual_pointer + 15, no_file_name)
		insert_bytes(actual_pointer + 16, actual_pointer + 24, no_size)
		insert_bytes(actual_pointer + 25, actual_pointer + 30, no_init_cluster)
		insert_bytes(actual_pointer + 31, actual_pointer + 45, no_date)
		insert_bytes(actual_pointer + 46, actual_pointer + 60, no_date)
		actual_pointer = actual_pointer + 64
	
	


def get_existing_files():
	global disk_name
	''' 
	Por la forma en la que trabaja el sistema se debe obtener una lista con los 
	nombres de archivos. 
	'''
	file_system_disk = open(disk_name,'r')
	actual_pointer_aux = init_dir
	'''
	 
	'''
	while actual_pointer_aux < 5120:
		file_system_disk.seek(actual_pointer_aux)
		query = file_system_disk.read(15)
		if query != 'AQUI_NO_VA_NADA':
			file_names.append(query.replace(" ",""))
			file_system_disk.seek(actual_pointer_aux+16)
			file_sizes.append(int(file_system_disk.read(8)))

			file_position = 0 
			for i in range(len(file_content_locator)):
				file_position += file_sizes[i] + 4

			file_position += 5120

			file_content_locator.append(file_position)

		actual_pointer_aux = actual_pointer_aux + 64

	actual_pointer_aux = 5120
	
	


	file_system_disk.close()
