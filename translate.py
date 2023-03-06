from googletrans import Translator
import sys

def main():
    print(input_data())

def input_data():

            print(f"\nEnter languages in abbreviated form (en, fr , cs , ru ) or in full (English, French, Czech, Russian)\n")

            from_lang = input("What language do you want to translate from: ")
            to_lang = input("What language do you want to translate into: ")
            return translate_test(from_lang, to_lang)


def translate_test(from_lang, to_lang):
        try:
            text = input(f"Text: ")
            print()
            translator = Translator()
            translation = translator.translate(text=text, src=from_lang, dest=to_lang)
            print(translation.text)
            ab(from_lang,to_lang)
        except Exception:
            print(f"The languages you wrote are not properly written or are not supported.\n")
            input_data()


def ab(from_lang,to_lang):

    while True:
        try:
            a = input(f"\n*If you want to exit print /1/\n*If you want to change language print /2/"
                      f"\n*If you want continue translate just print text\nText: ")
            print()
            if a == '/1/':
                sys.exit()
            elif a == '/2/':
                input_data()
            else:
                translator = Translator()
                translation = translator.translate(text=a, src=from_lang, dest=to_lang)
                print(translation.text)
        except Exception:
            print('some mistake')

if __name__ == '__main__':
    main()


