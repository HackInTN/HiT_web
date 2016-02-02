from subprocess import call, check_output, STDOUT

def create_docker(image):
	return check_output(["docker", "run", "-d", image], stderr=STDOUT)\
	       .decode()[:-1]

def get_docker_ip(docker_id):
	return check_output(["docker", "inspect", "-f", "\"{{ .NetworkSettings.IPAddress }}\"",
						docker_id], stderr=STDOUT).decode()[1:-2]

def stop_docker(docker_id):
	call(["docker", "stop", docker_id])
	call(["docker", "rm", docker_id])
