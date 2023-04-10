# QRKot — приложение благотворительного фонда поддержки котиков. Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции. Текущий проект - API к приложению.

## Проекты:
У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.

## Пожертвования:
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

## Пользователи
Целевые проекты создаются администраторами сайта. 
Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых.
Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

## Проект создан с использованием FastAPI.

## Для установки проекта на локальной машине руководствуйтесь следующими рекомендациями: 

**Клонировать репозиторий и перейти в него в командной строке:**

```
git clone 
```

```
cd cat_charity_fund
```

**Cоздать и активировать виртуальное окружение:**

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

**Установить зависимости из файла requirements.txt:**

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

**Основные эндпоинты:**

Charity Projects

Получение списка всех проектов.
__GET /charity_project/__

Создание нового проекта.
__POST /charity_project/__
*только для зарегистрированного пользователя.*

Удаление проекта.
__DELETE /charity_project/{project_id}__
*только для Суперпользователя.*

Редактирование проекта.
__PATCH /charity_project/{project_id}__
*только для Суперпользователя.*


Donations

Получение списка все пожертвований.
__GET /donation/__ 
*только для Суперпользователя.*

Создание пожертвования.
__POST /donation/__
*только для зарегистрированного пользователя.*

Получение списка своих пожертвований.
__GET /donation/my__
*только для зарегистрированного пользователя.*


Auth

Авторизация в системе.
__POST /auth/jwt/login__

Выйти из системы.
__POST /auth/jwt/logout__

Регистрация в системе.
__POST /auth/register__

Редактирование пользовательского аккаунта.
__POST /users/{id}__
