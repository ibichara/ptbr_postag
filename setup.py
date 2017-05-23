from distutils.core import setup

setup(
	name ="ptbr_postag",
	packages = ["ptbr_postag"],
	version = "0.4",
	description = "Part-of-Speech tagging module for brazilian portuguese language",
	author = "Igor Bichara",
	author_email = "igor.coutinho@tvglobo.com.br",
	url = "https://github.com/ibichara/ptbr_postag",
	download_url = "https://github.com/ibichara/ptbr_postag/archive/0.4.tar.gz",
	keywords = ['nlp', 'postag', 'postagging'],
	install_requires = ['nltk'],
	classifiers = [])
