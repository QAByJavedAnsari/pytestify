import subprocess

def check_docker():
    try:
        # Run `docker info` and check the return code
        subprocess.run(["docker", "info"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    if not check_docker():
        print("Docker is not running. Please start Docker and try again.")
