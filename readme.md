# img_edit

img_edit - это консольная программа для выполнения простых операций с изображениями с использованием модуля OpenCV. Программа поддерживает обрезку, поворот, масштабирование, отзеркаливание, размытие и увеличение резкости изображений. 

## Возможности

- Обрезка изображений
- Поворот изображений
- Масштабирование изображений
- Отзеркаливание изображений
- Размытие изображений
- Увеличение резкости изображений
- Загрузка и обработка нескольких файлов одновременно
- Полноценное консольное меню
- Проверка на возможные исключения
- Сохранение файлов с указанием пути и имени, включая текущую дату и время

## Установка

1. Убедитесь, что у вас установлен Python 3.x.
2. Установите необходимые зависимости:
    ```bash
    pip install opencv-python
    ```

## Использование

1. Запустите программу:
    ```bash
    python img_edit.py
    ```
2. Следуйте инструкциям в консольном меню для выполнения операций с изображениями.

## Пример сохранения файла

При сохранении файла, от пользователя требуется указать путь и имя файла. К имени файла будет добавляться текущая дата и время в формате `image-27.11-10.12.jpg`.

## Принципы разработки

- 1 функция - 1 действие: каждая функция выполняет только одну операцию для упрощения кода и улучшения читаемости.

## Лицензия

Этот проект лицензирован под лицензией MIT. Подробности см. в файле LICENSE.

## Вклад

Если вы хотите внести вклад в проект, пожалуйста, создайте форк репозитория и отправьте pull request. Мы приветствуем любые предложения и улучшения!

---
