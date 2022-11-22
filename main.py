from random import shuffle
from json import load
from rich.table import Table
from rich.console import Console
from os import system
from platform import system as os
from string import ascii_lowercase

def clear():
    if os() == "Windows":
        system('cls')
    else:
        system('clear')

def ask_question(question):
    clear()

    # Generate options (a, b, c..)
    CHOICES = []
    for i in range(len(question['options']) + 1):
        CHOICES.append(ascii_lowercase[i])

    # Make a shuffled array of options mixed with answer
    options = question["options"]
    options.append(question["answer"])
    shuffle(options)

    console.print(f"[white]{question['question']}")
    for option in options:
        console.print(f"[white]{CHOICES[options.index(option)]}:[/white] [cyan]{option}")
    
    answer = input(f"{CYAN}> {GREEN}")

    correct_option = CHOICES[options.index(question['answer'])]
    if answer in CHOICES:
        # if their answer is in the choices list
        return (True, correct_option == answer, correct_option)
    else:
        return (False, None, correct_option)
    

def quiz(questions):
    correct_answers = 0
    incorrect_answers = 0
    for question in questions:
        valid, correct, right_answer = ask_question(question)
        if valid:
            if correct:
                correct_answers += 1
                console.print("[green]Correct!")
            else:
                console.print("[red]Incorrect!")
                console.print(f"[white]The correct answer is [green]{right_answer}) {question['answer']}")
                incorrect_answers += 1
        else:
            console.print(f"[white]That is not a valid option\nWill be marked as [red]INCORRECT")
            incorrect_answers += 1
        
        input()
    return correct_answers, incorrect_answers


if __name__ == '__main__':
    with open("quiz.json") as file:
        questions = load(file)

    CYAN = '\033[36m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    DEFAULT = '\033[0m'
    console = Console()

    correct = 0
    incorrect = 0
    total = len(questions)


    correct, incorrect = quiz(questions)
    clear()
    print("\n\n\n")

    table = Table(title=f"{CYAN}Results")

    table.add_column("[cyan]Marks[/cyan]", style="cyan", justify="center")
    table.add_column("[cyan]Percentage[/cyan]", style="cyan", justify="center")
    table.add_column("[green]Correct[/green]", style="green", justify="center")
    table.add_column("[red]Incorrect[/red]", style="red", justify="center")
    table.add_column("[cyan]Total Questions[/cyan]", style="cyan", justify="center")
    
    total = incorrect + correct
    table.add_row(
        f"{correct}/{total}",
        str(round((correct / (total)) * 100, 2)) + '%',
        str(correct),
        str(incorrect),
        str(total),
    )

    console.print(table)