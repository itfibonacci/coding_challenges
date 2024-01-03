from server import server_thread

if __name__ == "__main__":
	server_thread.start()
	server_thread.join()