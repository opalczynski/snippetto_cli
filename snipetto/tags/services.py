from snipetto.core.services import CoreServices


class TagsService:
    tags_list = CoreServices.get_tags_list_url()

    @classmethod
    def list_tags(cls):
        pass
