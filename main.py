import os
import subprocess

# Создание папок Encode, Decode, Encode_Result и Decode_Result
os.makedirs('Encode', exist_ok=True)
os.makedirs('Encode_Result', exist_ok=True)

input_image = './Encode/input_image.png'
output_audio = './Encode_Result/output.wav'

# Список кодеров и декодеров
coders_decoders = [
    "MartinM1", "MartinM2", "ScottieS1", "ScottieS2", "ScottieDX", "Robot36",
    "PasokonP3", "PasokonP5", "PasokonP7", "PD90", "PD120", "PD160", "PD180",
    "PD240", "PD290", "WraaseSC2120", "WraaseSC2180", "Robot8BW", "Robot24BW"
]

while True:
    # Вывод списка команд
    print("ЭТО ТЕСТОВАЯ ПРОГРАММА!")
    print("Создатель: ChernilkaDev")
    print("Выберите команду:")
    print("0 - Выxод")
    print("1 - Декодировать сигнал")
    print("2 - Кодировать изображение")
    print("3 - Помощь")
    choice = input("Введите номер команды: ")
    
    # Обработка выбора пользователя
    if choice == "0":
        exit()
    elif choice == "1":
        print("Не работает.")
    elif choice == "2":
        print("Выберите SSTV Кодер")
        print("Доступные кодеры:")
        break  # Выход из цикла, если выбор верный
    elif choice == "3":
        print("")
        print("Чтобы Кодировать изображение нужно:")
        print("1. В папку Encode нужно поместить png файл с именем input_image(результат: input_image.png)")
        print("2. Выберите команду \"Кодировать изображение\"")
        print("3. Выберите номер кодера")
        print("4. В папке Encode_Result будет результат декодирования.")
        print("")
        print("ВАЖНО: Размер изображения для кодирования должно быть таким:")
        print("")
        print("320x240:")
        print("- Robot36")
        print("- Robot8BW")
        print("- Robot24BW")
        print("")
        print("320x256:")
        print("- MartinM1")
        print("- MartinM2")
        print("- ScottieS1")
        print("- ScottieS2")
        print("- ScottieDX")
        print("- PD90")
        print("- WraaseSC2120")
        print("- WraaseSC2180")
        print("")
        print("640x496:")
        print("- PasokonP3")
        print("- PasokonP5")
        print("- PasokonP7")
        print("- PD120")
        print("- PD180")
        print("- PD240")
        print("")
        print("512x400:")
        print("- PD160")
        print("")
        print("800x616:")
        print("- PD290")
        print("")
    else:
        print("Неверный выбор. Попробуйте снова.")

# Вывод списка кодеров или декодеров
for i, coder_decoder in enumerate(coders_decoders, start=1):
    print(f"{i}. {coder_decoder}")

while True:
    select_coder = input(f"Введите номер {choice == '1' and 'декодера' or 'кодера'}: ")
    
    # Проверка, корректный ли ввод
    if select_coder.isdigit() and 1 <= int(select_coder) <= len(coders_decoders):
        selected_coder = coders_decoders[int(select_coder) - 1]
        print(f"Выбранный {choice == '1' and 'декодер' or 'кодер'}: {selected_coder}")
        
        # Сохранение выбранного кодера или декодера в переменной mode
        mode = selected_coder
        
        # Кодирование или декодирование
        if choice == "2":
            # Кодирование
            command = ['python', '-m', 'pysstv', '--mode', mode, input_image, output_audio]
            subprocess.run(command)
        break  # Выход из цикла, если выбор верный
    else:
        print("Неверный выбор. Попробуйте снова.")
