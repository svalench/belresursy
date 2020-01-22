from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
# Create your views here.
from apps.vesovay.models import Auto
from setting_common import USER_ROLES_SETTINGS
from vzveshivanie.views import AbsView


class AbsAuthSkladView(AbsView):

    def _response_with_permissions(self, dispatch_response, request, *args, **kwargs):

        if not hasattr(dispatch_response, 'status_code') or dispatch_response.status_code == 302:
            return dispatch_response

        elif (not request.user or not request.user.client or (request.user.client.user_role == USER_ROLES_SETTINGS[0][0])or (request.user.client.user_role == USER_ROLES_SETTINGS[1][0])):
            return self.handle_no_permission()
        else:
            return dispatch_response


class StartSkladView(AbsAuthSkladView):

    template_name = 'sklad/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request,**kwargs):
        auto = Auto.objects.all().order_by('id')
        context = {'auto': auto}
        return render(request, self.template_name, context)

    def forma(request,id):
        auto = Auto.objects.filter(id=id)
        auto = auto[0]
        context = {'auto': auto}
        return render(request, 'sklad/forma.html', context)