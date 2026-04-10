# Команда проекта
Тройнина Алеся
Саев Матвей
Кириллова Анна

В рамках парсинга данных с Youtube APU были взяты данные о компаниях из топа бигтех компаний и по каждой компании доставал по 20 видео для каждого из следующих запросов:
• Компания + работа IT
• Компания + стажировка IT',
• Компания + ' карьера IT

Сначала были собраны данные с [сайта топа бигтех компаний на 2024 год](https://smartranking.ru/ru/ranking/big-tech/#:~:text=Table_title:%20%D0%A0%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3%20%D0%BA%D1%80%D1%83%D0%BF%D0%BD%D0%B5%D0%B9%D1%88%D0%B8%D1%85%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9%20BigTech%20100,%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B%20%D0%BE%D1%82%20Ozon%20%D0%91%D0%B0%D0%BD%D0%BA%2C%20Ozon%20Travel.%20%7C) 
Далее помощью цикла совершался проход по всем компаниям из данного списка начиная с лучшей компани (Яндекса) и по каждой компании формировался запрос на самые популярнрые видео по запросу Компания + ключевое слово (ключевые слова описаны выше).
Сбор совершался до тех пор, пока не закончится лимит по данному ключу. В итоге удалось собрать 2725 видео по топ 30 компаний для дальнешего анализа.

### Использованные эндпоинты:
Youtube API:
'https://www.googleapis.com/youtube/v3/search' - для первичного поиска видео по запросу Компания + ключевое слово
'https://www.googleapis.com/youtube/v3/videos' - для дополнения инфоормацией о самом видео
'https://www.googleapis.com/youtube/v3/channels' - для дополнения инфой о канале-авторе
'https://www.googleapis.com/youtube/v3/videoCategories' - для того, чтобы подтянуть информацию о категориях видео

Wordstat API:
'https://searchapi.api.cloud.yandex.net/v2/wordstat/topRequests' - для получения статистики упоминаний основных запросов по каждой компании среди запросов по трудоустройству


### Основные ссылки на использованные источники:
#### Youtube API
1) Официальная страница для получения Api ключа: https://developers.google.com/youtube/v3?hl=ru
2) Документация о работе с Yutube API: https://vtemah.livejournal.com/1474650.html 
3) Метрика интересности видео: https://habr.com/ru/companies/vdsina/articles/533080/ 

#### Wordstat API
1) Аккаунт для привязки API ключа: https://center.yandex.cloud/billing/accounts/dn2zptmz7g77hvyuwgea/overview
2) Создание лицевого счета: https://yandex.cloud/ru/docs/billing/concepts/personal-account 
3) Управление API ключами: https://yandex.cloud/ru/docs/iam/operations/authentication/manage-api-keys#api_2 
4) Документация по работе с Wordstat API: https://osipenkov.ru/api-wordstat/ 

5) Данные за последние 30 дней о популярных запросах, содержащих указанное ключевое слово, и запросах, похожих на указанное: https://aistudio.yandex.ru/docs/en/search-api/api-ref/Wordstat/getTop.html 


#### Top-100 Bigtech
1) https://smartranking.ru/ru/ranking/big-tech/#:~:text=Table_title:%20%D0%A0%D0%B5%D0%B9%D1%82%D0%B8%D0%BD%D0%B3%20%D0%BA%D1%80%D1%83%D0%BF%D0%BD%D0%B5%D0%B9%D1%88%D0%B8%D1%85%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D1%85%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9%20BigTech%20100,%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B%20%D0%BE%D1%82%20Ozon%20%D0%91%D0%B0%D0%BD%D0%BA%2C%20Ozon%20Travel.%20%7C 

