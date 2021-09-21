from abc import ABC, abstractmethod
import os
class FlatCubeWriter(ABC):
    @abstractmethod
    def getColorScheme(self):
        pass

    def writeCube(self, description):
        colorScheme = self.getColorScheme()
        lines = description.split("\n")
        colorized = ""
        for line in lines:
            colorized += self.colorize(line, colorScheme) + "\n"
        return colorized
    
    def colorize(self, text, colorScheme):
        colorized = ""
        previous = ''
        for current in text:
            if previous != current:
                colorized += colorScheme[current]
            colorized += "■" if current != ' ' else ' '
            previous = current
        return colorized + colorScheme["__EndColor__"]

class FullColorConsoleFlatCubeWriter(FlatCubeWriter):
    def getColorScheme(self):
        color_scheme = {
            "U": "[38;2;200;200;200m",
            "R": "[38;2;255;0;0m",
            "D": "[38;2;255;255;0m",
            "L": "[38;2;255;165;0m",
            "F": "[38;2;0;255;0m",
            "B": "[38;2;0;165;255m",
            " ": "",
            "__EndColor__": "[0m"
            }
        return color_scheme

class LegacyConsoleFlatCubeWriter(FlatCubeWriter):
    def getColorScheme(self):
        color_scheme = {
            "U": "[37m",
            "R": "[31m",
            "D": "[33m",
            "L": "[35m",
            "F": "[32m",
            "B": "[34m",
            " ": "",
            "__EndColor__": "[0m"
            }
        return color_scheme

class FlatCubeWriterFactory:

    @classmethod
    def createFlatCubeWriter(self, type = "auto"):
        if type.lower() == "auto":
            type = self.getTerminalColorType()

        if type.lower() == "legacy":
            return LegacyConsoleFlatCubeWriter()
        elif type.lower() == "fullcolor":    
            return FullColorConsoleFlatCubeWriter()
        else:
            raise Exception(f"unable to instantiate FlatCubeWriter of unknown type '{type}'")

    @classmethod
    def getTerminalColorType(self):
        fullColors = self.isFullcolorSupported()
        if fullColors:
            type = "fullcolor"
        else:
            type = "legacy"
        return type

    @classmethod
    def isFullcolorSupported(self):
        # Generic Unix terminal
        if self.isEnvironment("TERM", "xterm-color"):
            return True
        # Visual Studio Code embedded terminal
        if self.isEnvironment("TERM_PROGRAM", "vscode"):
            return True
        # Windows terminal
        if "WT_SESSION" in os.environ:
            return True
        return False
    
    @classmethod
    def isEnvironment(self, name, value):
        if name in os.environ:
            if os.environ[name] == value:
                return True
        return False