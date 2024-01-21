# For single XML to CSV File

# Import necessary modules
import csv 
import xml.etree.ElementTree as ET

# Define a function for converting XML to CSV
def xml_to_csv(file_path, csv_name) -> None:
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Open the CSV file for writing
    with open(csv_name, 'w') as csv_file:
        # Create a CSV writer
        writer = csv.writer(csv_file)
        
        # Extract headers from the first child element of the XML root
        headers = (child.tag for child in root[0])
        
        # Write the headers to the CSV file
        writer.writerow(headers)
        
        # Get the number of records in the XML file
        num_records = len(root)
        
        # Iterate through each record and write it to the CSV file
        for record in range(num_records):
            rec = (child.text for child in root[record])
            writer.writerow(rec)

# Check if the script is being run as the main program
if __name__ == '__main__':
    # Import additional modules
    import sys
    import pathlib
    
    try:
        # Get the XML file path and CSV file name from command line arguments
        file_path = sys.argv[1]
        csv_name = sys.argv[2]
        
    except IndexError:
        # Exit the program if the required arguments are not provided
        sys.exit('Two arguments required: one XML path and one save file name.')
        
    # Create a pathlib.Path object for the XML file
    with pathlib.Path(file_path) as xml_file:
        # Check if the XML file exists
        if xml_file.is_file():
            # Call the xml_to_csv function to convert XML to CSV
            xml_to_csv(xml_file, csv_name)
            
        else:
            # Exit the program if the XML file is not found
            sys.exit(f'Did not find {file_path}')
