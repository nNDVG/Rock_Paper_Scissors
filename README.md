# Rock-Paper-Scissors (JetBrains Academy's project)
## Description
#### This is improved version of the game stone-paper-scissors. 
Before the start of the game, the user will be able to choose the options that will be used. After entering his/her name, the user should provide a list of options separated by a comma. For example, rock,paper,scissors,lizard,spock. If the user inputs an empty line, your program should start the game with default options: rock, paper, and scissors. After the game options are defined, your program should output Okay, let's start. Whatever list of options the user chooses, your program, obviously, should be able to identify which option beats which, that is, the relationships between different options. First, every option is equal to itself (causing a draw if both the user and the computer choose the same option). Secondly, every option wins over one half of the other options of the list and gets defeated by another half. How to determine which options are stronger or weaker than the option you're currently looking at? Well, you can try to do it this way: take the list of options (provided by the user or the default one). Find the option for which you want to know its relationships with other options. Take all the options that follow this chosen option in the list. Add to them the list of options that precede the chosen option. Now you have another list of options that doesn't include the "chosen" option and has a different order of elements in it (first go the options following the chosen one in the original list, after them are the ones that precede it). So, in this "new" list, the first half of the options will be defeating the "chosen" option, and the second half will get beaten by it. For example, the user's list of options is rock,paper,scissors,lizard,spock. You want to know what options are weaker than lizard. By looking at the list spock,rock,paper,scissors you realize that spock and rock will be beating the lizard, and paper and scissors will get defeated by it. For spock it'll be almost the same, but it'll get beaten by rock and paper, and prevail over scissors and lizard. Of course, this is not the most efficient way to determine which option prevails over which. You are welcome to try to develop some other methods of tackling this problem. 

## Tech stach:
- Python 3.x
- Random

## Run 
It should be started from terminal by: python rock_paper_scissors.py

## Author

    https://github.com/nNDVG/

## Contacts

    Telegram: nNDVG
    Email: n.dvg@yandex.ru
