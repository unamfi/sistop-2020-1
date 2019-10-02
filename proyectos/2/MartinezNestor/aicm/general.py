from threading import Semaphore

mutex = Semaphore(1)

track = Semaphore(0)

planes = []
landing_tracks = []