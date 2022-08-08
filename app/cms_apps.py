from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class MainApphook(CMSApp):
    app_name = 'app'
    name = "Main Apphook"

    def get_urls(self, page=None, language=None, **kwargs):
        return ['app.urls']

