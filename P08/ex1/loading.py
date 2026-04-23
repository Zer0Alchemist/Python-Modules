import importlib  # import importlib to import modules dynamically


def check_packages() -> bool:
    # valid tracks if all packages are imported successfully
    # True if yes, False if no
    valid = True
    try:
        # importing pandas module, if it isnt downloaded
        # we raise an ImportError and give valid False value
        pd = importlib.import_module("pandas")
        print(f"[OK] {pd.__name__} ({pd.__version__}) - "
              "Data manipulation ready")
    except ImportError:
        print("[ERROR]: you must download the pandas package!")
        valid = False
    try:
        # importing requests module, if it isnt downloaded
        # we raise an ImportError and give valid False value
        requests = importlib.import_module("requests")
        print(f"[OK] {requests.__name__} ({requests.__version__}) - "
              "Network access ready")
    except ImportError:
        print("[ERROR]: You must download the requests package!")
        valid = False
    try:
        # importing matplotlib module, if it isnt downloaded
        # we raise an ImportError and give valid False value
        plt = importlib.import_module("matplotlib")
        print(f"[OK] {plt.__name__} ({plt.__version__}) - "
              "Visualization ready")
    except ImportError:
        print("[ERROR]: You must download thematplotlib package!")
        valid = False
    try:
        # importing numpy module, if it isnt downloaded
        # we raise an ImportError and give valid False value
        numpy = importlib.import_module("numpy")
        print(f"[OK] {numpy.__name__} ({numpy.__version__}) - "
              "Generation ready")
    except ImportError:
        print("[ERROR]: You must download the numpy package!")
        valid = False

    return valid


def analyse_data() -> None:
    # We give valid what check_packages returned:
    # either True / False
    valid = check_packages()
    print("\nAnalyzing Matrix data...")
    # Checking if valid is false (prints whats in it on the way)
    if valid is False:
        raise ImportError("Couldn't Process data : a package is not imported")
    else:
        # we import the modules again and give them an alias
        pd = importlib.import_module("pandas")
        plt = importlib.import_module("matplotlib.pyplot")
        numpy = importlib.import_module("numpy")

        # we generate and arrange 1000 numbers
        player_id = numpy.arange(1, 1001)
        # we generate random ints that cannot excceed 40
        # 1000 times
        goals = numpy.random.randint(0, 40, 1000)
        # organizing the data into a pandas DataFrame (table
        dt_frame = pd.DataFrame({
            "player_id": player_id,
            "goals": goals,
        })
        print("Processing 1000 data points...")

        # creating an empty figure
        plt.figure()
        # we give the figure some bars
        # player ids down, goals on the left
        plt.bar(dt_frame["player_id"], dt_frame["goals"])
        # we save and create an image that showcase
        # all players and their goals
        plt.savefig("matrix_analysis.png")

        print("\nAnalysis complete!")
        print("Result saved to: matrix_analysis.png")


if __name__ == "__main__":
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")
    try:
        analyse_data()
    except ImportError as e:
        print(e)
