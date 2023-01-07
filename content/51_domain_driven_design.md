Title: Domain Driven Design
Date: 2022-12-10 21:00
Category: architecture
Tags: microservices, ddd
Author: Andrey G
Status: published
Summary: domain driven design или предметно-ориентированное проектирование
Lang: ru
---

![Domain-Driven Design](/images/20190111151118821.png){: .image-process-big-article-image}


Для себя хочу иметь заметку про DDD в которой кратко будет все что нужно занать про DDD.
"кратко" - это, скорее всего, не возможно в формате заметки или даже целой статьи... Но почему бы и не попробовать.

[Domain-Driven Design: Everything You Always Wanted to Know About it, But Were Afraid to Ask](https://medium.com/ssense-tech/domain-driven-design-everything-you-always-wanted-to-know-about-it-but-were-afraid-to-ask-a85e7b74497a)

[Агрегаты](https://habr.com/ru/post/660599/)

[Domain-driven design: рецепт для прагматика](https://habr.com/ru/company/jugru/blog/440772/)

[DDD: Strategic Design: Core, Supporting, and Generic Subdomains](https://blog.jonathanoliver.com/ddd-strategic-design-core-supporting-and-generic-subdomains/)

[Как приручить DDD. Часть 1. Стратегическая](https://habr.com/ru/company/oleg-bunin/blog/650927/)

[Как приручить DDD. Часть 2. Практическая](https://itnan.ru/post.php?c=1&p=661129)


# Что такое DDD ?

Много разных определений на все вкусы:

> Domain-Driven Design - это борьба со сложностью бизнес-процессов и их автоматизации и реализации в коде

> Domain-Driven Design - это единый язык между экспертами и программистами

> Domain-Driven Design - это набор принципов и схем, направленных на создание оптимальных систем объектов.
    Сводится к созданию программных абстракций, которые называются моделями предметных областей.
    В эти модели входит бизнес-логика, устанавливающая связь между реальными условиями области применения продукта и кодом.

> Domain-Driven Design - is a major software design approach, focusing on modeling software to match a domain according
    to input from that domain's experts.

> Domain-Driven Design - is an approach to software design that glues the system’s implementation to a constantly evolving model,
    leaving aside irrelevant details like programming languages, infrastructure technologies, etc…


# Как это работает?

Из определений становится немного понятней, что DDD - это некий подход к проектированию приложений который основа
на том что мы в первую очередь выражаем в коде сущности из предметной области.
И надеимся что очередной рефакторинг или новый состав команды не убьет нашу идею.
"описываем сущности из предметной области" - в идеале значит что эксперт смотрящий в наш код должен видеть в нем сушности из своего мира.

Мы на верном пути к DDD если в обсуждениях фич, бизнес-логики люди используют термины которые и для разработчиков
и для экспертов имеют одинаковое значение.


### Немного деталей как устроено DDD


- __Domain__ / Домен - глобальная предметная область

- __Subdomain__ / Поддомен - бизнес задача, обладают высокой связностью

    - __Core__ - конкурентное преимущество компании

    - __Supporting__ - не является уникальных знанием компании но без этого все еще нельзя существовать

    - __Generic__ - типовые задачи которые могут быть делегированы третьим лицам, компании

    - __Bounded context__ / Границ поддомена - это ограниченная часть системы, в которой мы реализуем нашу бизнес-логику

- __Entity__ / Сушность - объект у которого есть уникальный идентификатор. Например: покупатель, заказ.

- __Value Object__ / Объект-значение  - объект который описывает характеристики. это атрибуты и они могут быть частью нескольких Entity. Например: адрес.

- __Aggregates__ / Агрегаты -  это кластер сущностей и объектов-значений, объединённых общими инвариантами.
Любое взаимодействие с агрегатом осуществляется через одну и только одну из его сущностей, называемую корнем агрегата.


DDD и микросервисы
![Domain-Driven Design and microservices](/images/Screenshot 2023-01-07 233506.png){: .image-process-big-article-image}


# Паттерны

[__PDF__, PATTERNS, PRINCIPLES, AND PRACTICES OF DOMAIN-DRIVEN DESIGN](/books/Patterns_Principles_and_Practices_of_Domain-Driven_Design_(2015).pdf)

# Особенности и проблемы DDD

- Хорошо подходит для редкоменяющихся, налаженных бизнес-процессов

- Много доменных моделей лучше чем одна елинственна на все приложение. Меньше боли при изменениях.
Внутри компании могут быть разные понимания одних терминов, процессов.

- Плохо масштабируется


# Книги

[Вон Вернон: Реализация методов предметно-ориентированного проектирования](https://www.labirint.ru/books/518957/)
[__PDF__, Implementing Domain-Driven Design](/books/AW.Implementing.Domain-Driven.Desig.pdf)

[Эрик Эванс: Предметно-ориентированное проектирование (DDD). Структуризация сложных программных систем](https://www.labirint.ru/books/512940/)
[__PDF__, Domain -Driven Design TACKLING COMPLEXITY IN ТНЕ HEART OFSOFTWARE](/books/Эрик_Эванс_Предметно_ориентированное.pdf)

[книги по ссылкам здесь](https://habr.com/ru/post/660599/)

[Modern Software Architecture: Domain Driven Design](https://medium.com/modern-software-architecture/modern-software-architecture-1-domain-driven-design-f06fad8695f9)
