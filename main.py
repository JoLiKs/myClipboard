import asyncio

import keyboard

from main import times
import pyperclip

class AIter:   #упрощенный аналог range для async for
    def __init__(self, N):
        self.i = 0
        self.N = N

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        #print(f"start {i}")
        await asyncio.sleep(0.7)
        #print(f"end {i}")
        if i >= self.N:
            raise StopAsyncIteration
        self.i += 1
        return i
c = 0
first_data = ''
second_data = ''

def get_selected_text():
    global first_data, second_data, c
    # Получаем текст из буфера обмена
    selected_text = pyperclip.paste()
    print(c)
    if c == 0:
        first_data = selected_text
        c +=1
    elif c == 1:
        second_data = selected_text
        c = 0

def paste_second():
    global first_data, second_data, c
    keyboard.write(second_data)

def paste_first():
    global first_data, second_data, c
    keyboard.write(first_data)

keyboard.add_hotkey("ctrl+c", get_selected_text)
keyboard.add_hotkey("ctrl+s", paste_first)
keyboard.add_hotkey("ctrl+q", paste_second)


async def run():
    async for i in AIter(65):
        await asyncio.sleep(0.5)


asyncio.run(run())


