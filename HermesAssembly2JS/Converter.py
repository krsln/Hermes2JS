import os

from HermesAssembly2JS.Hermes2JS.FileOps import ProcessFile, GetFiles
from HermesAssembly2JS.Hermes2JS.Logger import logger


def main():
    """Main function to process specific section_<number>.hbc files."""
    logger.info("Starting .hbc to JavaScript conversion")
    input_dir = "../Test/Sections"
    output_dir = "../Test/JS"

    # input_dir = "../Apps/Testy/Sections"
    # output_dir = "./Apps/Testy/JS"

    # Ensure input directory exists
    if not os.path.exists(input_dir):
        logger.error(f"Input directory does not exist: {input_dir}")
        return

    files = GetFiles(input_dir, output_dir)
    # files = GetFiles(input_dir, output_dir, start=9594, end=9600)
    # files = GetFiles(input_dir, output_dir, start=11946, end=11946)
    if not files:
        logger.info("No .hbc files found.")
        return

    logger.info(f"Found {len(files)} .hbc files in {input_dir}\n")
    for filename, section_index in files:
        logger.info(f"Processing section #{section_index}: {filename}")
        file_path = os.path.join(input_dir, filename)
        ProcessFile(section_index, file_path, output_dir)

    logger.info("Conversion completed successfully")


if __name__ == "__main__":
    main()
