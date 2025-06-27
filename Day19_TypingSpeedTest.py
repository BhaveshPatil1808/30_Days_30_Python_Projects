from time import time

def tperror(prompt, inprompt):
    prompt_words = prompt.split()
    input_words = inprompt.split()
    error = 0
    for i in range(min(len(prompt_words), len(input_words))):
        if prompt_words[i] != input_words[i]:
            error += 1
    # Count extra words typed or missed
    error += abs(len(prompt_words) - len(input_words))
    return error

def calc_speed(inprompt, stime, etime):
    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / (etime - stime) * 60
    return round(speed, 2)

def elapsed_time(stime, etime):
    return round(etime - stime, 2)

if __name__ == '__main__':
    prompt = ("Python is an interpreted, high-level, general-purpose "
              "programming language. Created by Guido van Rossum and first released in "
              "1991, Python's design philosophy emphasizes code readability with its "
              "notable use of significant whitespace. Its language constructs and object "
              "oriented approach.")

    print("Type this:\n", prompt)
    input("\nPress Enter when you are ready to check your speed...")

    stime = time()
    inprompt = input("\nStart typing here:\n")
    etime = time()

    elapsed = elapsed_time(stime, etime)
    typing_speed = calc_speed(inprompt, stime, etime)
    errors = tperror(prompt, inprompt)

    print("\n--- Results ---")
    print("Total time elapsed:", elapsed, "seconds")
    print("Your Average Typing Speed:", typing_speed, "words per minute (wpm)")
    print("Total Errors:", errors)
