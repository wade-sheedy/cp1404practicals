

from prac_07.programming_langauge import ProgrammingLangauage


def main():

    ruby = ProgrammingLangauage("Ruby", "Dynamic", "Yes", 1995)
    python = ProgrammingLangauage("Python", "Dynamic", "Yes", 1991)
    visual_basic = ProgrammingLangauage("Visual Basic", "Static", "NO", 1991)
    languages = [ruby.__str__(), python.str(), visual_basic.__str__()]
    for i in range(len(languages)):
        print(languages[i])


main()