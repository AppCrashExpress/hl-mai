# Контекст решения
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

Person(user, "Пользователь")
Person(commodity_manager, "Менеджер продуктов")

System(store_site, "Сайт магазина", "Сайт для заказов продуктов онлайн")

Rel(user, store_site, "Взаимодействует с сайтом: регистрируется, просматривает продукты, создает заказы")
Rel(commodity_manager, store_site, "Добавляет новые товары и редактирует цены/количество существующих")

@enduml
```
## Назначение систем
|Система| Описание|
|-------|---------|
| Сайт магазина | Для конечных пользователей представляет собой веб-интерфейс, в котором доступны соответствующих для пользователя прав (заказ для пользователя и добавления заказа для менеджера) |