from HermesAssembly2JS.Splitter.hermes_splitter import HermesAssemblyFileSplitter

if __name__ == "__main__":
    app = "Coachify"
    # app = "Testy"
    input_file = f"../Apps/{app}/Output/output.hbc"  # Path to your 68MB .hbc file .hbc
    output_dir = f"../Apps/{app}/Sections"  # Directory to store output files

    HermesAssemblyFileSplitter(input_file, output_dir)
