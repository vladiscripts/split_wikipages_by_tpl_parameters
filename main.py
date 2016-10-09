#!/usr/bin/env python3
# coding: utf8
#
# author: https://github.com/vladiscripts
#
import re
import mwparserfromhell
import pywikibot

listpages_filename = 'listpages.txt'  # список страниц для обработки
var_template = ('ВАР')


def pagetitle_target(title):
	""" Форматер названия второй страницы """
	# Строка ниже создаёт:
	# 'Страница:Lobachevsky (Syn otechestva).djvu/3' → 'Страница:Lobachevsky (Syn otechestva).djvu:ВТ/3'
	# 'Страница:Lobachevsky (Syn otechestva).djvu' → 'Страница:Lobachevsky (Syn otechestva).djvu:ВТ'
	addon = ':ВТ'
	npages = r'(/\d+)$'
	if re.search(npages, title):
		title_new = re.sub(npages, addon + r'\1', title)
	else:
		title_new = title + addon

	# title_new = 'Участник:Vladis13/test second'  # тест страница
	return title_new


def file_readlines_in_list(filename):
	from sys import version_info
	PYTHON_VERSION = version_info.major
	if PYTHON_VERSION == 3:
		f = open(filename, encoding='utf-8')
	else:
		import codecs
		f = codecs.open(filename, 'r', encoding='utf-8')
	arr_strings = f.read().splitlines()
	f.close()
	# чистка пустых строк
	for v in arr_strings:
		if v.isspace() or v == '':
			arr_strings.remove(v)
	return arr_strings


def file_readlines_in_set(filename):
	arr_strings = set(file_readlines_in_list(filename))
	return arr_strings


def remove_parameters(wikicode, tpl_name, param_name):
	for tpl in wikicode.filter_templates():
		if tpl.name.matches(tpl_name):
			param = tpl.get(param_name).value if tpl.has(param_name) else None
			wikicode.replace(tpl, param)
	return wikicode


site = pywikibot.Site('ru', 'wikisource')

listpages = file_readlines_in_set(listpages_filename)
for title_origin in listpages:
	if title_origin == '': continue

	# Открытие страниц
	page1 = pywikibot.Page(site, title_origin)
	text_original = page1.get()
	# text_original = file_readtext('wikipage.txt')  # тест, вики-страница из файла

	title2 = pagetitle_target(title_origin)
	page2 = pywikibot.Page(site, title2)

	# Парсинг
	wikicode1 = mwparserfromhell.parse(text_original)
	page1.text = str(remove_parameters(wikicode1, var_template, 1))

	wikicode2 = mwparserfromhell.parse(text_original)
	page2.text = str(remove_parameters(wikicode2, var_template, 2))

	# Запись страниц
	edit_comment1 = 'перенесено на ' + '[[' + title2 + ']]'
	page1.save(edit_comment1)
	edit_comment2 = 'перенесено из ' + '[[' + title_origin + ']]'
	page2.save(edit_comment2)

	pass
