while True:
    phrase = str(input("Write your sentence: ")).lower()
    words = phrase.split(" ")
    words_glue = ""
    siglas = ["!", "?", ",", ".", ":", ";"]
    try:
        for word in words:
            if word[-1] in siglas:
                words_glue += word[0:-1]
            else:
                words_glue += word        
        print(words_glue == words_glue[::-1])
    except:
        print("Invalid value, input a valid sentence")
