## Тестовое задание на позицию Backend разработчик [Toothless Consulting Inc](https://toothless.co/about/)

В проекте используется платежная система [Stripe](stripe.com/docs) с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей.
### Запуск
Запуск производится командой `docker-compose up`
### Работа с сервисом
Сервер работает на `http://localhost`

Эндпоинты:

**Выдача обработанных данных**
1. Метод: **GET** `http://localhost/buy/{id}`
    
   В ответе содержится поле “response” с `Stripe Session Id` для оплаты выбранного `Item`.

2. Метод: **GET** `http://localhost/item/{id}`

   HTML страница с информацией о выбранном `Item` и кнопкой `Buy`. По нажатию кнопки Buy происходит запрос на `/buy/{id}`, получение `Stripe Session Id` и редирект на Checkout форму Stripe.
