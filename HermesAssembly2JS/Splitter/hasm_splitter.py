import re
import argparse
from pathlib import Path


def HermesAssemblyFileSplitter(input_file, output_dir):
    """
    Splits a .hasm file into separate files based on '===============' separators.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    function_pattern = re.compile(r'^\[Function #(\d+)\s+"([^"]*)"\s+of\s+\d+\s+bytes\]')
    current_section = []
    section_count = 0
    function_number = None
    function_name = None

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.rstrip()

                if stripped_line == '===============':
                    if current_section:
                        if function_number is not None:
                            filename = f"function_{function_number}_{function_name or 'anonymous'}.hasm"
                        else:
                            filename = f"section_{section_count}.hasm"

                        filename = "".join(c if c.isalnum() or c in '_-.' else '_' for c in filename)
                        output_path = output_dir / filename

                        try:
                            with open(output_path, 'w', encoding='utf-8') as out_f:
                                out_f.write(''.join(current_section))
                            print(f"Created: {output_path}")
                        except Exception as e:
                            print(f"Error writing {output_path}: {e}")

                        section_count += 1
                        current_section = []
                        function_number = None
                        function_name = None
                    continue

                current_section.append(line)

                if not function_number:
                    match = function_pattern.match(stripped_line)
                    if match:
                        function_number = match.group(1)
                        function_name = match.group(2) or None

            # Handle the last section
            if current_section:
                if function_number is not None:
                    filename = f"function_{function_number}_{function_name or 'anonymous'}.hasm"
                else:
                    filename = f"section_{section_count}.hasm"

                filename = "".join(c if c.isalnum() or c in '_-.' else '_' for c in filename)
                output_path = output_dir / filename

                try:
                    with open(output_path, 'w', encoding='utf-8') as out_f:
                        out_f.write(''.join(current_section))
                    print(f"Created: {output_path}")
                except Exception as e:
                    print(f"Error writing {output_path}: {e}")

                section_count += 1

        print(f"✅ Total sections created: {section_count}")

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"❌ Error processing file: {e}")


def main():
    parser = argparse.ArgumentParser(description="Split a Hermes .hbc file into sections.")
    parser.add_argument('--input', '-i', type=str, required=True, help='Path to input .hbc file')
    parser.add_argument('--output', '-o', type=str, required=True, help='Output directory for sections')

    args = parser.parse_args()
    HermesAssemblyFileSplitter(args.input, args.output)


if __name__ == "__main__":
    main()
