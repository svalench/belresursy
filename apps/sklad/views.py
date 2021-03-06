from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
# Create your views here.
from apps.sklad.models import Agent
from apps.vesovay.models import Auto, Vagon
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

class AbsAuthAdminView(AbsView):

    def _response_with_permissions(self, dispatch_response, request, *args, **kwargs):

        if not hasattr(dispatch_response, 'status_code') or dispatch_response.status_code == 302:
            return dispatch_response

        elif (not request.user or not request.user.client or (request.user.client.user_role == USER_ROLES_SETTINGS[0][0]) or (request.user.client.user_role == USER_ROLES_SETTINGS[1][0]) or (request.user.client.user_role == USER_ROLES_SETTINGS[3][0])):
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
        vagon = Vagon.objects.all().order_by('id')
        context = {'auto': auto,'vagon':vagon}
        return render(request, self.template_name, context)

    def forma(request,id):
        auto = Auto.objects.filter(id=id)
        agent = Agent.objects.all().order_by('id')
        auto = auto[0]
        print(agent)
        context = {'auto': auto,'agent':agent}
        return render(request, 'sklad/forma.html', context)

    def addAgent(request):
        agent = Agent.objects.all().order_by('id')
        context = {'agents': agent}
        return render(request, 'sklad/addagent.html', context)

class AddAgentView(AbsAuthSkladView):
    template_name = 'sklad/addagent.html'

    def post(self, request, *args, **kwargs):
        form = self.request.POST
        address = form['address-city'] + ", " + form['address-street']
        ag = Agent(name = form['name'], address = address, unp= form['unp'], description=form['description'])
        ag.save()
        print(ag)
        return redirect('sklad:addagent')

class Setting(AbsAuthAdminView):
    template_name = 'setting.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = {'agents': ''}
        return render(request, 'setting.html', context)