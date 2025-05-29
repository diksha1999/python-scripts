import subprocess

# Replace these with your actual details
user = input("Enter the username: ")
kubeadmin_password = input("Enter the kubeadmin password: ")
api_server_url = input("Enter the APIserver endpoint to login to the cluster: ")

def login_to_oc():
    try:
        # Build the command
        login_command = [
            "oc", "login",
            api_server_url,
            "-u", user,
            "-p", kubeadmin_password,
            "--insecure-skip-tls-verify"
        ]

        # Run the command
        result = subprocess.run(login_command, check=True, capture_output=True, text=True)
        print("Login successful!")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Login failed!")
        print(e.stderr)

login_to_oc()
