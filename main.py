
from Trainer import Trainer

#TODO: Add CLI interface with option of doing the input prompts, switch train mode to integers
def main():
    print("Welcome to the Deutsch Trainer!")
    train_mode = input("Please select a training mode (Vocabulary, Articles): ")
    lesson_length = int(input("Please enter the number of words for this lesson: "))
    
    trainer = Trainer(train_mode, lesson_length)
    print(trainer.lesson_vocab)

    for word, answer in trainer.present_word():
        input(f"What is the {train_mode} of {word}? ")
        print(f"The correct answer is: {answer}")

if __name__ == "__main__":
    main()