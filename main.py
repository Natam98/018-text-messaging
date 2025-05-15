def convert_message_to_key_presses(message: str) -> str:
    message:str=message.upper()
    keypress_sequence:str=''
    
    key_press_mapping:dict[str, str]={
        "1":".,?!:",
        "2":"ABC",
        "3":"DEF",
        "4":"GHI",
        "5":"JKL",    
        "6":"MNO",
        "7":"PQRS",
        "8":"TUV",
        "9":"WXYZ",
        "0":" "
    }
    for character in message:
        for key,value in key_press_mapping.items():
            if character in value:
                character_index:int=value.index(character)
                keypress_sequence+=key*(character_index+1)
                break
            
    return keypress_sequence

def main():
    input_message=input("Enter a message: ")
    keypress_sequence:str=convert_message_to_key_presses(input_message)
    
    print(f"{input_message} = {keypress_sequence}")


if __name__=="__main__":
    main()