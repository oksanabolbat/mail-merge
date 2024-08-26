#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

NAME_MERGE = "[name]"

with open("./Input/Names/invited_names.txt") as invited_file:
    invited_names = invited_file.read().split('\n')

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()


if len(invited_names) > 0:
    for invited_name in invited_names:
        invited_name = invited_name.strip()
        invited_email_content = letter_template.replace(NAME_MERGE, invited_name)
        with open(f"./Output/letter_for_{invited_name}.docx", mode="w") as invited_email:
            invited_email.write(invited_email_content)

