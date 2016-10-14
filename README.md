# split_wikipages_by_tpl_parameters

Разделяет страницу с {{ВАР}} шаблоном на две, по параметрам шаблона (ДО и СО). Делает копию страницы, а затем заменяет в оригинальной шаблоны {{ВАР}} их первыми пераметрами, а во второй статье — вторыми параметрами.

Зависимости. Требует установки:
* pywikibot
* mwparserfromhell
Рекомендутся устанавливать development-версию фреймворка mwparserfromhell, которая имеет последние фиксы, см. описание в рамочке по ссылке:
http://mwparserfromhell.readthedocs.io/en/latest/index.html#installation
Для чего желательно установить Git (https://ru.wikipedia.org/wiki/Git) c https://git-scm.com/.

Запуск.
1. Внести в файл listpages.txt список страниц
2. Запустить "python splitpages.py"

Настройки.
* listpages_filename - файл со списком страниц для обработки
* функция pagetitle_target() - форматирование заголовка целевой страницы
* edit_comment1, edit_comment2 - комментарии к правкам
