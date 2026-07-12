from conversion.splitter.hermes_splitter import HermesAssemblyFileSplitter

if __name__ == "__main__":
    app = "Coachify"
    # app = "Testy"
    input_file = f"../apps/{app}/output/output.hbc"  # Path to your 68MB .hbc file .hbc
    output_dir = f"../apps/{app}/sections"  # Directory to store output files

    HermesAssemblyFileSplitter(input_file, output_dir)
