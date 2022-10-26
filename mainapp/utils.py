menu = [
    {'title': "Добавить статью", 'url_name': 'add_page'},
]

class DataMixin:
    
    def get_all_context(self, **kwargs):
        context = kwargs
        all_menu = menu.copy()
        context['menu'] = all_menu
        return context
