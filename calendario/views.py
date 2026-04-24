from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .models import Evento
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import json

@method_decorator(ensure_csrf_cookie, name='dispatch')
class CalendarioView(TemplateView):
    template_name = "index.html"


class EventoListView(View):
    def get(self, request):
        eventos = Evento.objects.all()
        data = [
            {
                "id": e.id,
                "title": e.titulo,
                "start": str(e.data),
                "color": e.cor
            }
            for e in eventos
        ]
        return JsonResponse(data, safe=False)


class EventoCreateView(View):
    def post(self, request):
        body = json.loads(request.body)

        evento = Evento.objects.create(
            titulo=body.get("title"),
            data=body.get("date"),
            cor=body.get("color")
        )

        return JsonResponse({"status": "ok", "id": evento.id})