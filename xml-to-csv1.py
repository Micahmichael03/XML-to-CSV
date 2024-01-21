import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

# Function to convert XML files to a Pandas DataFrame in CSV format
def xml_to_csv(path):
    # List to store data from XML files
    xml_list = []
    
    # Loop through each XML file in the specified path
    for xml_file in glob.glob(path + '/*.xml'):
        # Parse the XML file using ElementTree
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        # Extract information for each object in the XML file
        for member in root.findall('object'):
            # Get relevant data for each object
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,  # Object class
                     int(member[4][0].text),  # xmin
                     int(member[4][1].text),  # ymin
                     int(member[4][2].text),  # xmax
                     int(member[4][3].text)   # ymax
                     )
            xml_list.append(value)
    
    # Define column names for the DataFrame
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    
    # Create a Pandas DataFrame from the list of extracted values
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    
    # Return the DataFrame
    return xml_df

# Main function
def main():
    # Loop through two folders: 'train' and 'test'
    for folder in ['train', 'test']:
        # Construct the image path based on the current working directory
        image_path = os.path.join(os.getcwd(), ('images/' + folder))
        
        # Convert XML files in the current folder to a Pandas DataFrame
        xml_df = xml_to_csv(image_path)
        
        # Save the DataFrame to a CSV file in the 'images' folder
        xml_df.to_csv(('images/' + folder + '_labels.csv'), index=None)
    
    # Print a success message
    print('Successfully converted xml to csv.')

# Call the main function when the script is executed
main()
