def vault_sec(file_name1: str, file_name2: str):
    print("Initiating secure vault access...")
    try:
        with open(file_name1, "r") as file1, open(file_name2, "r") as file2:
            extra = file1.read()
            prev = file2.read()
        print("Vault connection established with a failsafe protocols\n")

        print("SECURE EXTRACTION:")
        print(extra)

        print("\nSECURE PRESERVATION:")
        print(prev)
        print("Vault automatically sealed upon completion\n")

        print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Couldn't extract/preserve Vault informations")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    vault_sec("classified_data.txt", "security_protocols.txt")
