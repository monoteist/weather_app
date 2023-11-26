# Weather App

Проект Weather App предоставляет два сервиса: API для получения погоды по названию города и телеграм-бот для получения погоды.

## Установка и запуск

### Docker

Cкачайте и установите: `Docker` и `Docker-Compose` если у вас `Linux`

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/monoteist/weather_app.git
    cd weather_app
    ```

2. Создайте файл `.env` на основе `example.env`:

    ```bash
    cp example.env .env
    ```

    Отредактируйте `.env`, установив необходимые значения переменных.

3. Запустите Docker Compose:

    ```bash
    docker-compose up --build
    ```

    Эта команда создаст и запустит контейнеры для вашего приложения.

4. Приложение будет доступно по адресу [http://localhost:8000/](http://localhost:8000/).

## Использование API

API для получения погоды доступно по эндпоинту `/api/v1/weather/`. Вы можете отправлять GET-запросы с параметром `city` для получения информации о погоде в указанном городе.

Пример запроса:

```bash
curl http://localhost:8000/api/v1/weather/?city=Москва
```