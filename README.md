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
Further on the structure and settings of the settings file.json

This column is responsible for the settings of the key:
```
"buttons": {
"d": [ <- In this case, the "d" button will be pressed if it is the same as the color written below
164, <- R
116, <- G
21 <- B
]...
```
In this column, you need to enter the pixel coordinates for scaning, however, this parameter should be prescribed only if ``"coordinatesratio" : false``` 
```
"coordinates": [
973,
920
],
```
If it is true, it will calculate the coordinates of the point using the formula, if your monitor isn't 1920x1080, it may cause errors!
Also note that this parameter takes the default point that is on the button in the expanded game window (not Fullscreen or borderless, namely the window mode in full screen)
``"coordinatesratio": true``

Monitor parameters, FullHD by default
``
"monitor": [
1920,
1080
],
```
The parameter needed for fine tuning outputs all the colors of the readable pixel, taking into account the filter for grayscale.
This parameter may cause errors in the display of keystrokes (The keys will be pressed normally, but on the console screen, they will look broken).
``"outputcolor": false``
