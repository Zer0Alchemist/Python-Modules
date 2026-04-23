def ancient_txt(file_name: str):
    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, "r")
        print("Connection established...\n")

        print("RECOVERED DATA:")
        print(file.read())

        file.close()
        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    ancient_txt("ancient_fragment.txt")
