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
        return "Je ne sais pas encore répondre à cette question."

    def conversation(self):
        print("Bonjour !")
        self.charger_base_de_donnees()  
        while True:
            question = input("Vous: ")
            reponse = self.repondre(question)
            print("AI: ", reponse)

            feedback = input("AI: Ai-je bien répondu ? (Oui/Non) ")
            if feedback.lower() == "non":
                nouvelle_reponse = input("AI: D'accord, quelle devrait être la réponse correcte ? ")
                self.apprendre(question, nouvelle_reponse)
                print("AI: Merci, j'ai appris quelque chose de nouveau !")

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.conversation()