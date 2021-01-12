from translate import Translator
translator=Translator(to_lang="Spanish")
translation = translator.translate("Good Morning! But also hello world.")
engTxt = "\nEnglish:\nGood Morning! But also hello world.\n"
spanTxt = "\nSpanish:\n"
print(engTxt + spanTxt + translation + "\n")
