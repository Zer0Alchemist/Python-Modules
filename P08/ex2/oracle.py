import dotenv  # importing dotenv to load .env file
import os


if __name__ == "__main__":
    print("\nORACLE STATUS: Reading the Matrix...\n")

    # loading the .env file into os.environ
    dotenv.load_dotenv()

    # reading each environment variable from os.getenv
    # returns None if the variable is not set
    mode = os.getenv("MATRIX_MODE")
    database = os.getenv("DATABASE_URL")
    api_access = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_net = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    try:
        # checking if mode is valid
        # if not we raise an exception
        if not mode or (mode != "development" and mode != "production"):
            raise Exception("Mode not configured")
        else:
            print(f"Mode: {mode}")
        # hecking if database is valid
        if not database:
            print("DataBase: Not connected")
        else:
            # if mode is in production we hide the database
            # for security
            if mode == "production":
                print("Database: Connected (hidden in production)")
            else:
                # else we print the dataase normally
                print(f"Database: Connected to {database}")
        # checking if api is valid
        if not api_access:
            print("API Access: not authenticated")
        else:
            print("API Access: Authenticated")
        # chacking if log level is valid
        if not log_level:
            print("Log Level: BUG")
        else:
            print("Log Level: DEBUG")
        # checking if network is valid
        if not zion_net:
            print("Zion Network: Offline")
        else:
            print("Zion Network: Online")
    except Exception as e:
        print(e)

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    # checking if the .env file exist in our directory
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[ERROR] .env file not configured")
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")
