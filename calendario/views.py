from django.views.generic import TemplateView, View
from django.http import JsonResponse
from .models import Evento, Tag
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
import json


@method_decorator(ensure_csrf_cookie, name='dispatch')
class CalendarioView(TemplateView):
    template_name = "index.html"


# ================= EVENTOS =================

class EventoListView(View):
    def get(self, request):
        tag_id = request.GET.get("tag")

        eventos = Evento.objects.select_related('tag')

        if tag_id:
            eventos = eventos.filter(tag_id=tag_id)

        data = [
            {
                "id": e.id,
                "title": e.titulo,
                "start": str(e.data),
                "color": e.tag.cor if e.tag else "#3788d8"
            }
            for e in eventos
        ]

        return JsonResponse(data, safe=False)


class EventoCreateView(View):
    def post(self, request):
        body = json.loads(request.body)

        tag = Tag.objects.get(id=body.get("tag"))

        evento = Evento.objects.create(
            titulo=body.get("title"),
            data=body.get("date"),
            tag=tag
        )

        return JsonResponse({"status": "ok", "id": evento.id})


class EventoUpdateView(View):
    def put(self, request, id):
        body = json.loads(request.body)
        evento = Evento.objects.get(id=id)

        evento.titulo = body.get("title")
        evento.data = body.get("date")
        evento.tag = Tag.objects.get(id=body.get("tag"))
        evento.save()

        return JsonResponse({"status": "updated"})


class EventoDeleteView(View):
    def delete(self, request, id):
        evento = Evento.objects.get(id=id)
        evento.delete()
        return JsonResponse({"status": "deleted"})


# ================= TAGS =================

class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        data = [
            {"id": t.id, "nome": t.nome, "cor": t.cor}
            for t in tags
        ]
        return JsonResponse(data, safe=False)


class TagCreateView(View):
    def post(self, request):
        body = json.loads(request.body)

        tag = Tag.objects.create(
            nome=body.get("nome"),
            cor=body.get("cor")
        )

        return JsonResponse({"id": tag.id})


class TagDeleteView(View):
    def delete(self, request, id):
        Tag.objects.get(id=id).delete()
        return JsonResponse({"status": "deleted"})