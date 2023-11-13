# beatbangerbot


## [RUS]

.exe файл - основной
.py файл  - source код 

Инструкция:
Скачайте файл формата .exe и запустите его в любой папке. Будет создан файл settings.json (если его нет), после чего программа предложит изменить его, 
после изменения (или игнорирования данного требования) нужно нажать Enter и бот автоматически запуститься
Дальше по структуре и настройки файла settings.json

Это колонка отвечает за настройки клавишь:
```
"buttons": {
		"d": [ <- В этом случае будет нажата кнопка "d", если она такая же как цвет написанный ниже
		164, <- R
		116, <- G
		21   <- B
		]...
```
В этой колонке нужно ввести координаты пикселя для считывания, однако этот параметр нужно прописывать, только в том случае, если ```"coordinatesratio" : false```
```
"coordinates": [
        973,
        920
    ],
```
Если стоит true будет рассчитывать координаты точки по формуле, в случае если ваш монитор не 1920x1080, может вызвать ошибки!
Также учтите, что этот параметр берёт точку по умолчанию, которая стоит на кнопке в развёрнутом окне игры (не Fullscreen или bordless, а именно оконный режим во весь экран)
```"coordinatesratio": true```

Параметры монитора, по умолчанию FullHD
```
"monitor": [
        1920,
        1080
    ],
```
Параметр нужный для точной настройки, выводит все цвета читаемого пикселя с учётом фильтра на оттенки серого.
Этот параметр может вызвать ошибки в отображении нажатия клавишь (Нажиматься клавиши будут нормально, но на экране консоли, они будут выглядить поломанно).
```"outputcolor": false```

## [ENG]

.exe file - main file
.py file - source code

Instruction manual:
Download the .exe file and run it in any folder. The settings.json file will be created (if there is none), after which the program will suggest changing it,
after changing (or ignoring this requirement) you need to press Enter and the bot will start automatically
Further on the structure and settings of the settings.json file

This column is responsible for the settings of the key:
```
"buttons": {
"d": [ <- In this case, the "d" button will be pressed if it is the same as the color written below
164, <- R
116, <- G
21 <- B
]...
```
In this column, you need to enter the pixel coordinates for scaning, however, this parameter should be prescribed only if ```"coordinatesratio" : false``` 
```
"coordinates": [
973,
920
],
```
If it is true, it will calculate the coordinates of the point using the formula, if your monitor isn't 1920x1080, it may cause errors!
Also note that this parameter takes the default point that is on the button in the expanded game window (not Fullscreen or borderless, namely the window mode in full screen)
```"coordinatesratio": true```

Monitor parameters, FullHD by default
```
"monitor": [
1920,
1080
],
```
The parameter needed for fine tuning outputs all the colors of the readable pixel, taking into account the filter for grayscale.
This parameter may cause errors in the display of keystrokes (The keys will be pressed normally, but on the console screen, they will look broken).
```"outputcolor": false```

## [@SufferinSufferin: in dumd terms]
Okay to help igorir3 out so people can figure it out a little easier ill try and make an easy to understand step by step.

Step 1. Go the github and down ***Just*** the .EXE file the py file is unnecessary. When you download the file put it into a folder by itself, i made a folder called "Bang beats Auto play" whatever works for you really

Step 2. Run the .Exe, this is easy as when you do this the .exe will create a setting  file for it run off of. This file is very important so do be careful when editing. If you happen to delete it, dont worry too much as the .exe file will make another one with a clean slate.

Step. 3 (somewhat optional)
Edit the setting files. This step is somewhat easy to understand if you understand what you are looking at. First open the new Settings File in ***Notepad*** as this the easiest way to see inside of it. Youll see a bunch jibberish that you can sort of make out. The buttons one is the most important as this what the file is telling the .exe to hit when the gane plays. Set the button to the same button you have set in ***Your*** copy of the game. The buttons in order from top down should be 1 2 3 and then 4. So dont get confused by the rgb color codes when you do.

For the rest of the stuff in the setting file dont worry too much if you have a Monitor in 1920x1080. Its automatically set so you dont have to do anything. If you dont have a monitor in 1920x1080. I cant help you cause i dont have a monitor that isnt 1920x1080 so i dont know your struggles (This Means, Good luck bois its a free for all)

Step 4. Run Beat banger in windows mode. This one looks fairly simple but with a little trick. Dont open the game in windows borderless or fullscreen just default windowed. After your screen will shrink down to small windowed application. This part is important, **DO NOT INCREASE THE ASPECT RATIO MANUALLY**. you know how you can change the aspect ratio in windowed mode back to 1920x1080 in the games menu. Dont do that. Instead use the "Enlarge windows button" like you would on an internet browser in the top right corner of the windowed game. The game should enlarge to fit the screen and after this should be smooth sailing

Step 5. Run the .exe alongside the game. After all those steps the .exe should be working fine and the bot should do its thing when you start a stage. Try it and it should work even on the hardest stages. Youll know the bot works when it .exe application window you see the button presses show up even if they press the wrong button (which would only happen if you didnt set the button properly)

I hopes this saves some of igorir3's time. Will try and make a more comprehensive step by step when im not at work and infront of my computer. Ill add visuals later as well.
