import random

class ChatBot:
    def __init__(self):
        self.database = {}  
        self.mots_cles = {}  

    def apprendre(self, question, reponse):
        self.database[question] = reponse
        self.mots_cles[question] = set(question.split())  
        self.enregistrer_base_de_donnees() 

    def enregistrer_base_de_donnees(self):
        with open("base_de_donnees.txt", "w") as fichier:
            for question, reponse in self.database.items():
                fichier.write(f"{question}:{reponse}\n")

    def charger_base_de_donnees(self):
        try:
            with open("base_de_donnees.txt", "r") as fichier:
                lignes = fichier.readlines()
                for ligne in lignes:
                    question, reponse = ligne.strip().split(":")
                    self.database[question] = reponse
                    self.mots_cles[question] = set(question.split())
        except FileNotFoundError:
            pass

    def repondre(self, question):
        for q, mots_cles in self.mots_cles.items():
            if all(mot in question for mot in mots_cles):
                return self.database[q]
        return "I don't yet know how to answer that question."

    def conversation(self):
        print("Hello !")
        self.charger_base_de_donnees()  
        while True:
            question = input("You: ")
            reponse = self.repondre(question)
            print("AI: ", reponse)

            feedback = input("AI: Did I answer correctly? (y/n) ")
            if feedback.lower() == "n":
                nouvelle_reponse = input("AI: Okay, what should the correct answer be? ")
                self.apprendre(question, nouvelle_reponse)
                print("AI: Thanks, I've learned something new !")

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.conversation()
