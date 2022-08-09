import time

from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

start_time = time.time()


def pdf_to_mp3(file_path='test.pdf', language='ru'):

    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':

        print(f'[+] Original file: {Path(file_path).name}')
        print('[+] Processing...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return f'[+] {file_name}.mp3 saved successfully!'

    else:
        return 'File not exists, check the file path!'


def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')
    file_path = input("\nEnter a file's path: ")
    language = input("Choose language, for example 'en' or 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))

    finish_time = time.time() - start_time
    print(f'Час виконання конвертації: {finish_time}')


if __name__ == '__main__':
    main()