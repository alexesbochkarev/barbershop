# Техническое задание на разработку сайта Барбершоп «Бородинский»

-   Название сайта: Барбершоп «Бородинский»
    
-   Домен: https://zloydedd.github.io/Barbershop/
    

### 



## **1. Общие технические требования**

-   1.1. Стандарты вёрстки: HTML5, CSS3, прогрессивное улучшение.
    
-   1.2. Сетка: определена в макете.
    
-   1.3. Адаптивность вёрстки: нет.
    
-   1.4. Используемые фреймворки: нет.
    
-   1.5. Кроссбраузерность: IE11+, Chrome, Firefox, Opera, Safari.
    
-   1.6. Типографика: частично определена в макете (прочее — на усмотрение разработчика).
    
-   1.7. Используемый шрифт: PT Sans Narrow (есть в папке с макетом и на Google Fonts).
    
-   1.8. С макетом предоставлен styleguide.psd, содержащий прорисовку состояний элементов интерфейса. При любых расхождениях с макетами он должен иметь наивысший приоритет.
    

 

## 2. Пояснения для учащихся

-   2.1. Часть макетов не включена в задание, дабы не усложнять его. Когда упомянуты страницы или элементы, отсутствующие в макетах, даны пояснения «макета нет, не делать». Такие элементы (модальное окно с фотографией, страница новостей и прочие) верстать не нужно.
    
-   2.2. В макетах есть скрытые слои с всплывающими окнами. Такие слои в блоке слоёв фотошопа выделены красным цветом.
    
-   2.3. Макеты верстаются постепенно, не нужно сразу выполнять все требования.
    

## 3. Пожелания к поведению блоков

#### Все макеты:

-   3.1. Контентная область центрируется и не может быть уже макетной ширины.
    
-   3.2. По клику на ссылку «вход» открывается модальное окно авторизации (смотрите папку слоёв «log in form» в barbershop-index.psd).
    
-   3.3. В блоке с хлебными крошками активная страница (последний пункт) не является ссылкой и не реагирует на наведение.
    
-   3.4. В пагинации активная страница не является ссылкой и не реагирует на наведение.
    
-   3.5. Нижняя часть страницы: предусмотрите появление ещё одной социальной кнопки.
    
-   3.6. Все кнопки в покое чёрные, по наведению меняют фоновый цвет — смотрите styleguide.psd.
    

#### barbershop-index.psd:

-   3.7. Логотип не является ссылкой.
    
-   3.8. Новостей может быть больше двух.
    
-   3.9. Картинки в фотогалерее — это ссылка, по клику открывается модальное окно с фотографией (макета нет, не делать).
    

#### barbershop-price.psd:

-   3.10. Добавление текста в контентные блоки не должно ломать страницу.
    

#### barbershop-shop.psd:

-   3.11. Фильтр (блоки «Производители» и «Группы товаров») верстать с помощью формы, кнопка «Показать» отвечает за отправку формы.
    
-   3.12. Количество товаров в правом блоке может быть любым, оно не должно ломать страницу.
    
-   3.13. Карточка товара: изображение товара — это ссылка на страницу товара.
    
-   3.14. Карточка товара: название товара — это ссылка на страницу товара (название состоит из двух строк, но по сути является одним блоком).
    
-   3.15. Карточка товара: кнопка «Купить» — по клику товар добавляется в корзину (макета корзины нет, не делать).
    

#### barbershop-item.psd:

-   3.17. При клике по миниатюре в галерее изображений большая фотография меняться не должна.
