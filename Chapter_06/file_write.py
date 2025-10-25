import os
# This program writes four lines of data
# to a file.


def main():
    # Open a file named philosophers.txt.
    outfile = open('Chapter06/philosophers.txt', 'w')

    # Alternative
    # Build the correct file path for any OS
    # filepath = os.path.join('Chapter_06', 'philosophers.txt')
    # outfile = open(filepath, 'w')

    # Write the names of three philosphers
    # to the file.
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    outfile.write('Immanuel Kant\n')

    # Close the file.
    outfile.close()


# Call the main function.
if __name__ == '__main__':
    # Checking default location
    print("Default location:", os.getcwd())
    main()
