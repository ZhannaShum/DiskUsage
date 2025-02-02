Визуализатор свободного места на диске.

Данный скрипт на языке программирования Python анализирует использование 
диска файловой системой и генерирует круговую диаграмму, 
показывающую распределение типов файлов. 

Скрипт использует модули os и shutil для получения информации о файловой системе 
и модуль matplotlib для создания круговой диаграммы.

Для запуска программы:
1. Убедитесь, что PyCharm установлен на вашем компьютере. Если нет, скачайте его 
с официального сайта: https://www.jetbrains.com/pycharm/download/
2. Склонируйте репозиторий с вашей программой из Git на свой компьютер. 
Вы можете использовать командную строку или любой другой инструмент Git, который вам нравится.
3. Откройте PyCharm и создайте новый проект, выбрав опцию "Create New Project" на стартовом экране.
4. Укажите название проекта и выберите интерпретатор Python. 
Если Python не установлен на вашем компьютере, укажите путь к нему.
5. Нажмите на кнопку "Open" внизу экрана, выберите папку с репозиторием на 
вашем компьютере и нажмите "OK".
6. Создайте новый файл Python внутри проекта, выбрав опцию "New" -> "Python File" в меню.
7. Откройте файл программы, которую вы хотите запустить, и нажмите на зеленую 
кнопку "Run" в правом верхнем углу редактора или используйте сочетание 
клавиш "Shift + F10", чтобы запустить программу.
8. Результат выполнения программы будет выведен в окне консоли PyCharm.

На выходе программа выведет круговую диаграмму, отображающую информацию о 
занятом и свободном месте на диске, а также создаст файл out.txt, в котором 
содержится информация о количестве файлов всех расширений
