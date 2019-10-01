from aicm.airport import Airport

def main(): 
	a = Airport("AICM: Benito Juárez", "Mexico City", n_tracks=4, n_buses=4, n_scooters=10,num_planes=5,num_operators=3)
	a.start()

if __name__ == "__main__":
	main()