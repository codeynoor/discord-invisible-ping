import keyboard
import pyperclip

payload = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||@everyone'
pyperclip.copy(payload)

def sendeveryone():
    keyboard.wait("'"); keyboard.press_and_release('backspace')
    keyboard.press('ctrl'); keyboard.press_and_release('v'); keyboard.release('ctrl')
    keyboard.press_and_release('enter')

def sendcustom():
    keyboard.wait("'"); keyboard.press_and_release('backspace'); keyboard.press_and_release('left'); keyboard.press_and_release('left')
    keyboard.press('ctrl'); keyboard.press_and_release('v'); keyboard.release('ctrl')
    keyboard.press_and_release('enter')

def main():
    print('\n[1] Invisible ping everyone')
    print('[2] Invisible ping user')
    mode = input('\nChoose an option: ')
    if mode == '1':
        print("\nType your message then press ' to send it!\nYou can exit by closing this window\n\nNOTE: The sent message has a spoilered bar visible, if you want to hide it, just end your message with any emoji.")
        while True:
            sendeveryone()
    elif mode == '2':
        print("\nType your message and tag someone then press ' to send it!You can exit by closing this window\n\nNOTE: The sent message has a spoilered bar visible, if you want to hide it, just end your message with any emoji.")
        while True:
            sendcustom()
    else:
        print('\nPlease choose a valid option!')
        main()



if __name__ == '__main__':
    main()
