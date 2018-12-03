from random import choice


questions = ["why is the sky blue?: ",
             "why is their a face on the moon?: ",
             "where are the dinosaurs?: ",
             "why are you using phone?: ",
             "do you have any games will you give me? "]

             
questions = choice(questions)
answer = input("why is the sky blue?: ").lower()

while answer != "just because":

    answer = input("Why?: ").strip().lower()

print("Oh......okay")

