#from urllib import response
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import joblib
import numpy as np

class DemoView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, *args, **kwarg):
        media_url = settings.MEDIA_ROOT
        model1 = joblib.load(f"{media_url}/model")
        data=request.data
        values_in = data.dict()
        values = [values_in['age'], values_in['ed'], values_in['employ'], values_in['debtinc'], values_in['creddebt'], values_in['othdebt']]
        values = list(map(int, values))
        l=np.asarray(values)
        pred = model1.predict_proba([l])
        pred_default=pred[0][1]
        if pred_default>0.2476080913770519:
            return JsonResponse({'response':'The person will Default its our recommendation not to give this person loan'})
        else:
            return JsonResponse({'response':'The person will not Default its our recommendation to give this person loan'})




