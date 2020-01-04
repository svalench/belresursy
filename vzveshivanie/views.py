import abc
import threading
from abc import ABCMeta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView

from cv2 import *
import numpy as np
from django.http import StreamingHttpResponse

from setting_common import USER_ROLES_SETTINGS, USER_SUCCESS_LOGIN_REDIRECTS_BY_USER_ROLE















class AbsView(LoginRequiredMixin, TemplateView, metaclass=ABCMeta):
    login_url = reverse_lazy('login')


    def dispatch(self, request, *args, **kwargs):
        response = super(AbsView, self).dispatch(request, *args, **kwargs)
        return self._response_with_permissions(response, request, *args, **kwargs)

    @abc.abstractmethod
    def _response_with_permissions(self, dispatch_response, request, *args, **kwargs):
        pass

def redidrec(request):
    if(request.user.is_anonymous):
        return HttpResponseRedirect(reverse('login'))
    else:
        response = redirect(USER_SUCCESS_LOGIN_REDIRECTS_BY_USER_ROLE[request.user.client.user_role])
    return response