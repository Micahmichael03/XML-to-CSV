﻿# XML-to-CSV

These script is designed to be run from the command line, taking the XML file path and desired CSV file name as arguments. It uses the ElementTree module to parse the XML file and csv module to write the data to a CSV file. The headers are extracted from the XML's first child element, and then each record is written to the CSV file. The script handles errors, such as missing command line arguments or non-existent XML files.
