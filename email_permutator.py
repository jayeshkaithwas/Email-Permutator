import argparse
import os
from permutations import email_permuter

def read_names_from_file(file_path):
    """Read names from a file and return a list of tuples (first_name, last_name)."""
    names = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Ignore empty lines
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    first_name, last_name = parts
                    names.append((first_name, last_name))
    return names

def generate_emails(first_name, last_name, domain_name):
    """Generate email permutations for given names and domain."""
    return email_permuter.all_email_permuter(first_name=first_name,
                                             last_name=last_name,
                                             domain_name=domain_name)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate email permutations from names in a file.")
    parser.add_argument('file', type=str, help='Path to the text file containing names')
    parser.add_argument('domain', type=str, help='Email domain name')
    parser.add_argument('-o', '--output', type=str, help='Path to the output file to save results')

    args = parser.parse_args()

    # Validate file path
    if not os.path.isfile(args.file):
        print(f"Error: The file {args.file} does not exist.")
        return

    # Read names from file
    names = read_names_from_file(args.file)

    output_lines = []

    # Process each name and generate email permutations
    for first_name, last_name in names:
        emails = generate_emails(first_name, last_name, args.domain)
        # Commenting out the print statement
        # print(f"Emails for {first_name} {last_name}:")
        for email in emails:
            output_lines.append(f"{email}")

    if args.output:
        with open(args.output, 'w') as outfile:
            outfile.write("\n".join(output_lines))
        print(f"Results have been written to {args.output}.")
    else:
        # Print the results to the console if no output file is specified
        for line in output_lines:
            print(line)

if __name__ == "__main__":
    main()
