Puzzle 1: Write to a File 
Create a file example.txt and write "Hello, World!" using w mode.

  def hey_hello():
      with open('example.txt', 'w') as file:
          file.write("Hello, World!")
   hey_hello()


Puzzle 2: Append to a File 
Append "This is an appended line." to example.txt.
  def append_line():
      with open('example.txt', 'a') as file:
        file.write("This is an appended line.")
   append_line()

Puzzle 3: Read a File 
Read and print the content of example.txt.

    def read_file():
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
    read_file()

Puzzle 4: Write and Read a File
Write "Python is fun!" to test.txt and read it

    def write_and_read():
        #write
        with open('test.txt', 'w') as file:
            file.write("Python is fun!")
    
        #read
        with open('test.txt', 'r') as file:
            content = file.read()
            print(content)
    write_and_read()

Puzzle 5: Append and Read 
Append "New data" to log.txt, then read the entire file

    def append_and_read():
        #append
        with open('log.txt', 'a') as file:
            file.write("New data")
    
    #read
        with open('log.txt', 'r') as file:
            content = file.read()
            print(content)
    append_and_read()




