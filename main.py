import asyncio
import keyboard
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

second_data = ''

def get_selected_text():
    global second_data
    # Получаем текст из буфера обмена
    selected_text = pyperclip.paste()
    second_data = selected_text


def paste_second():
    global first_data, second_data, c
    keyboard.write("\b\b"+second_data)

keyboard.add_hotkey("ctrl+c", get_selected_text)
keyboard.add_hotkey("c+v", paste_second)


async def run():

    async for i in AIter(6500):
        await asyncio.sleep(0.5)


asyncio.run(run())

