# Интернет магазин

---
## О чем проект?

- Данный проект реализовывает:
  - Работу с базой данных `postgres`
  - Работу с фреймоврком `Django` как с инструментом по созданию сайтов
  и бэкэнда сайта
  - Работа с front-end составляющей сайта используя библиотеку стилей `bootstrap`
## Что из себя представляет?

```
Сайт с авторизацией и возможностью авторизации, регистрации и аутентификации
и кастомизауией своего профиля
- Создание собственных постов и вещей которые вы хотите продать,
а так же редактировать и снимать их с публикации. Следить за просматриваемостью товара
и получать уведомление на почту по достижению 100 просмотров
Строгий доступ к управлению над товаром
```

## Как запустить?
1. Скопировать репозиторий к себе в среду разработки
2. Установка зависимотей:
   - ```bash
     pip install -r requirements.txt
     ```
   - Заполнить `.env` файл на основе `.env.sample`
   - Запустить проект:
   - ```bash
     python3 manage.py runserver
     ```

---
### Наглядно посмотреть на то как это выглядит можно тут:
![Главная страница](https://gultruekanekisss.github.io/internet_shop_django_hw/main_page.png)
![Войти](https://gultruekanekisss.github.io/internet_shop_django_hw/login.png)
![Регистрация](https://gultruekanekisss.github.io/internet_shop_django_hw/registration.png)
![Просмотр Товара](https://gultruekanekisss.github.io/internet_shop_django_hw/product_page.png)
![Публикация товара](https://gultruekanekisss.github.io/internet_shop_django_hw/public_product.png)
![Профиль](https://gultruekanekisss.github.io/internet_shop_django_hw/profile.png)
