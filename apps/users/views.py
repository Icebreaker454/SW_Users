from django.conf import settings
from django.core.paginator import Paginator
from django.views.generic import TemplateView

from data_access import DBWrapper


class UserListView(TemplateView):

    template_name = 'users/user_list.html'

    def get_user_list(self):
        wrapper = DBWrapper(**settings.DB_DATA)
        query = self.request.GET.get('search_query')
        if query:
            return wrapper.get_users_by_name(query)
        return wrapper.get_all_users()

    def paginate_users(self, users):
        try:
            paginate_by = int(self.request.GET.get('paginate_by', 15))
        except ValueError:
            paginate_by = 15
        paginator = Paginator(users, paginate_by)

        try:
            page = int(self.request.GET.get('page', 1))
        except ValueError:
            page = 1

        return paginator, paginator.page(page)

    def get_context_data(self, *args, **kwargs):
        ctx = super(UserListView, self).get_context_data(*args, **kwargs)
        users = self.get_user_list()
        paginator, page = self.paginate_users(users)
        ctx.update({
            'paginator': paginator,
            'page': page,
        })
        return ctx
