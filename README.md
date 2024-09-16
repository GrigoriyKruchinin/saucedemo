# Проект: Автоматическое тестирование сайта с помощью Playwright

## Описание проекта

Этот проект содержит автоматический тест для проверки сценария покупки товара на сайте [saucedemo.com](https://www.saucedemo.com/) с использованием библиотеки [Playwright](https://playwright.dev/). Тест выполняет следующие действия:

1. Авторизуется на сайте с использованием тестовых учетных данных.
2. Добавляет товар в корзину.
3. Оформляет покупку.
4. Проверяет успешное завершение заказа.

## Развертывание проекта

Следуйте этим инструкциям для развертывания и запуска проекта на вашем компьютере:

#### 1. Клонирование репозитория

Сначала клонируйте репозиторий с GitHub и перейдите в проект:

```
git clone https://github.com/GrigoriyKruchinin/saucedemo.git
cd saucedemo
```

#### 2. Создание виртуального окружения
Рекомендуется создать виртуальное окружение для управления зависимостями проекта:

```
python -m venv .venv
```

#### 3. Активируйте виртуальное окружение

```
source .venv/bin/activate
```

#### 4. Установка зависимостей Python
Установите зависимости, указанные в requirements.txt:


```
pip install -r requirements.txt
```

#### 5. Установка браузеров Playwright
После установки зависимостей, установите браузеры для Playwright:

```
playwright install
```

#### 6. Установка системных зависимостей (только для Linux)
Playwright требует установки системных библиотек для работы с браузерами. Выполните следующую команду, чтобы установить необходимые зависимости:

```
playwright install-deps
```

Эта команда устанавливает библиотеки, необходимые для корректного функционирования браузеров, которые Playwright использует для тестирования.



#### 7. Запуск тестов
Теперь вы можете запустить тесты:

```
python test.py
```

Тест выполнит сценарий, описанный в проекте, и выведет результаты в консоль.

## Примечания
- Убедитесь, что у вас установлены Python версии 3.11 или выше.
- Если у вас возникают проблемы с установкой или запуском тестов, проверьте, что все зависимости установлены корректно и выполнены все шаги из инструкции.