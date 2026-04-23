def arch_creation():
    print("Initializing new storage unit : new_discovery.txt")
    try:
        file = open("new_discovery.txt", "w")

        print("Storage unit created successfullly...\n")

        print("Inscribing preservation data...")
        data1 = "[ENTRY 001]New quantum algorithm discovered\n"
        data2 = "[ENTRY 002]Efficiency increased by 347%\n"
        data3 = "[ENTRY 003]Archived by Data Archivist trainee\n"

        file.write(data1)
        file.write(data2)
        file.write(data3)

        print(data1, end="")
        print(data2, end="")
        print(data3)

        file.close()
        print("Data inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except PermissionError:
        print("ERROR: Couldn't write on this file")


if __name__ == "__main__":
    arch_creation()
