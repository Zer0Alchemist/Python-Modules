def crisis_resp(file_name: str):
    try:
        with open(file_name, "r") as file:
            data = file.read()

        print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
        print(f"SUCCESS: Archive recovered - ``{data}``")
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("Crisis handled, security maintained\n")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("Crisis handled, security maintained\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_resp("lost_archive.txt")

    crisis_resp("classified_vault.txt")

    crisis_resp("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")
