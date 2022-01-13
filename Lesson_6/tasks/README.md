### Решить кейс:
Руководство решает внедрить фичу “С этим товаром покупают” в Интернет-магазине. Вам предлагается протестировать фичу на одном из товаров. Для тестирования фичи вам исходя из истории покупок в интернет-магазине нужно определить ТОП-10 наиболее близких товаров к исходному.
1. Используйте датасет с  практики текущего урока.
1. Создайте матрицу item-customer (по срокам - товары, по столбцам - покупатели)
1. Проведите оценку мер близости товаров, получив матрицу item_item_sim_matrix со значениями косинусов между векторами товаров.
1. Отберите ТОП-10 похожих товаров по StockCode.
1. Выведите список ТОП-10 похожих товаров с названиями (Description) на экран.  
                     
Исходный товар - StockCode: 23166 Description: MEDIUM CERAMIC TOP STORAGE JAR           
             