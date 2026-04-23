import sys


def stream_manage():
    id = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")

    sys.stdout.write(f"\n[STANDARD] Archive status from {id}: {report}\n")
    sys.stderr.write(
        "[ALERT] System diagnostic: "
        "Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")

    print("\nThree-channel communication test successful.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    stream_manage()
