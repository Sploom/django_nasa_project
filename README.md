# Тестовое задание

## Описание
Этот проект является веб-приложением, разработанным на стеке Python, Django и MySQL. Он предназначен для демонстрации базового landing page с возможностью просмотра фотографий в слайдере.

### Основные функции:
- Просмотр landing page с информацией и преимуществами.
- Просмотр фотографий в слайдере на главной странице.
- Управление фотографиями через админ-панель Django с использованием `django-filer`.

## Технологии
- **Python**
- **Django**
- **MySQL**
- **Bootstrap 5**
- **Slick Slider** [Подробнее о Slick Slider](https://github.com/kenwheeler/slick/).

## Установка и запуск проекта
Для работы с проектом необходимо иметь установленные Python и MySQL. После клонирования репозитория выполните следующие шаги:

1. Установите `pipenv`, если еще не установлен:
    ```bash
    pip install pipenv
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    pipenv shell
    ```

3. Установите зависимости проекта:
    ```bash
    pipenv install -r req.pip
    ```

4. Настройте подключение к базе данных MySQL в `settings.py`.

5. Примените миграции к базе данных:
    ```bash
    python manage.py migrate
    ```

6. Запустите проект:
    ```bash
    python manage.py runserver
    ```

7. Откройте `http://127.0.0.1:8000/` в вашем браузере, чтобы увидеть результат.


## Основное для доработки

### Версии технологий
В процессе разработки должны были использоваться Python 3.9 и Django 4.1. Однако, в ходе работы произошла установка Python 3.10.2 и Django 5.0.4. Хотя при установке в виртуальном окружении я указывал версии...

### Соответствие макету
Полное воссоздание макета из Figma не было достигнуто, особенно в части стилей и макета. Однако, старался сохранить общий стиль и концепцию оригинального дизайна.

### Адаптивность
Работа над мобильной версией показала значительные сложности, особенно с адаптацией слайдера. Несмотря на использование адаптивного фреймворка Bootstrap, слайдер Slick не удалось идеально настроить под мобильные устройства.

![alt](https://i.imgur.com/UJOAbgh.png)
