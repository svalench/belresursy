
import threading

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators import gzip
from django.views.generic import TemplateView, FormView
# Create your views here.
from apps.vesovay.forms import VesAvtoForm
from vzveshivanie.views import AbsView
from setting_common import USER_ROLES_SETTINGS
from cv2 import *
import numpy as np
from django.http import StreamingHttpResponse
class AbsAuthVesView(AbsView):

    def _response_with_permissions(self, dispatch_response, request, *args, **kwargs):

        if not hasattr(dispatch_response, 'status_code') or dispatch_response.status_code == 302:
            return dispatch_response

        elif (not request.user or not request.user.client or (request.user.client.user_role == USER_ROLES_SETTINGS[3][0]) or (request.user.client.user_role == USER_ROLES_SETTINGS[0][0])):
            return self.handle_no_permission()
        else:
            return dispatch_response





# #
# class VideoCamera:
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()
# #
#     def __del__(self):
#         self.video.release()
# #
#     def get_frame(self):
#         image = self.frame
#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
# #
#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()
#
#
# cam = VideoCamera()
# #
# def gen(camera):
#     while True:
#         frame = cam.get_frame()
#         yield(b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#
#
# @gzip.gzip_page
# def livefe(request):
#     try:
#         return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:  # This is bad! replace it with proper handling
#         pass












class StartVesView(AbsAuthVesView):
    template_name = 'vesovay/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VesAvtoForm()
        return context

class AddVesCarView( AbsAuthVesView):
    def post(self, request, *args, **kwargs):
        form = self.request.POST
        print(form)
    template_name = 'vesovay/index.html'