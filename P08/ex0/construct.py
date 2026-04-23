import sys  # importing the sys module for executable
import os  # importing the os for virtual env path
import site  # importing the site module for packages path


if __name__ == "__main__":
    # os.environ.get() to see if a new
    # v env environment variable is created
    # returns None of it isn't
    env_path = os.environ.get("VIRTUAL_ENV")

    if env_path is None:
        print("MATRIX STATUS: You're still plugged in\n")

        # printing the OLD executable path (normal bin path)
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")

        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows\n")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the consruct\n")

        # printing the NEW executable path (v env bin path)
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: matrix_env")

        # printing the v env path
        print(f"Environment Path: {env_path}\n")

        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        # printing all pip package installations in this environment
        print(site.getsitepackages())
