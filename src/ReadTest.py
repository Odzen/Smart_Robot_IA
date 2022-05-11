"""
Class ReadTest
"""

# Constants
nameToRead = "maze"
nameToWrite = "out"

class ReadAndWrite(object):
    def __init__(self, testNumber):
        self.nameToRead = nameToRead
        self.nameToWrite = nameToWrite
        self.testNumber = testNumber

    def input(self):       
        '''
        input()
        Function to read the file under the format established by the task. 
        The name is changed in the global variable "nameToRead". (Don't modify!)
        '''
        with open("../MazesTests/in/"+self.nameToRead+str(self.testNumber)+".txt", "r") as f:
            content = f.read().split('\n')
            lines = []
            width = len(content)
            for line in content:
                lines.append(list(map(lambda x: int(x), line.split(" "))))
            height = len(lines[0])
            return width, height, lines
    
    def output(self, output, testNumber):
        '''
        output()
        Function to write over the file as requested in the project.
        The file name is changed in the global variable "nameToWrite". (Do not modify method!)
        '''
        
        lines = output
        toWrite = ""
        for line in lines:
            toWrite += "\n" + str(line)
    
        with open("../MazesTests/out/"+self.nameToWrite+self.testNumber+".txt", "w") as f:
            f.write(toWrite)