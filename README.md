# split_wikipages_by_tpl_parameters

Разделяет страницу с {{ВАР}} шаблоном на две, по параметрам шаблона (ДО и СО). Делает копию страницы, а затем заменяет 
в оригинальной шаблоны {{ВАР}} их первым пераметром, а во второй статье — второй параметр.

Зависимости. Требует установки: 
* pywikibot
* mwparserfromhell 
Рекомендутся устанавливать development-версию mwparserfromhell, см. описание в рамочке по ссылке: 
http://mwparserfromhell.readthedocs.io/en/latest/index.html#installation
Для чего желательно установить Git (https://ru.wikipedia.org/wiki/Git) c https://git-scm.com/.

Настройки.
listpages_filename - файл со списком страниц для обработки
