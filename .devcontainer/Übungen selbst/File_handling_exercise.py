def main():
    try:
        with open("Chapter_06/numbers.txt") as infile:  #dem File einen Namen zuweisen
            contents = infile.read()                    #das bennante File lese mit infile.read
            tokens = contents.split()

    except FileNotFoundError as ex:
        print(f"The error is: {ex}")

    else:
        if not contents:                #not falls keine Daten in der Datei sind. 
            print("No data available")
        else: 
            print(contents)
            print("Count: ", len(tokens))

    finally:
        print("Good Bye")



# conditional execution
if __name__ == "__main__":
    main()