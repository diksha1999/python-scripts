import subprocess
import sys # To help determine the OS for the command

def main():
    # Determine the command based on the operating system
    if sys.platform.lower().startswith('win'):
        command = ['dir']
    else: # For Linux, macOS, etc.
        command = ['ls', '-l']

    print(f"Running command: {' '.join(command)}")

    try:
        # Use subprocess.run() here
        # Make sure to capture output and decode it as text.
        result = subprocess.run(command, capture_output=True, text=True) # We can add check=True later

        # Print the captured standard output
        print("\nOutput from command:")
        print(result.stdout)

        # Print the return code
        print(f"\nCommand finished with return code: {result.returncode}")

        if result.returncode == 0:
            print("Command executed successfully!")
        else:
            print(f"Command failed with error (if any):\n{result.stderr}")

    except FileNotFoundError:
        print(f"Error: The command '{command[0]}' was not found. Is it installed and in your PATH?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

print(sys.version_info)