class Dictionary:
    def __init__(self):
        self.adj = ""
        self.noun = ""
        self.verb = ""
        self.adverb = ""
       
    def set_properties(self):
         self.adj = input("Adjective: ")
         self.noun = input("Noun: ")
         self.verb = input("Verb: ")
         self.adverb= input("Adverb: ")   
        
    def mad_lib(self):
        print(f"A(n) {self.adj} {self.noun} {self.verb} {self.adverb}") 
        

dictonaryClass = Dictionary()

dictonaryClass.set_properties()
dictonaryClass.mad_lib()     