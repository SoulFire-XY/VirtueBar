#################################
# SYMBOL TABLE
################################

class SymbolTable:
    def __init__(self):
        self.symbols = {} # global Vars
        self.parent = None # Local Vars e.g:- Inside function

    def get(self, name):
        value = self.symbols.get(name, None)

        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]