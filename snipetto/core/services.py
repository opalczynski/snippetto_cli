import requests

from settings.common import SNIPETT_MAPPING_URL


class CoreServices:
    @classmethod
    def get_mapping(cls):
        return requests.get(SNIPETT_MAPPING_URL).content

    @classmethod
    def get_tags_list_url(cls):
        return cls.get_mapping()['tags']['list']

    @classmethod
    def get_snippets_detail_url(cls):
        return cls.get_mapping()['snippets']['detail']

    @classmethod
    def get_snippets_list_url(cls):
        return cls.get_mapping()['snippets']['list']
