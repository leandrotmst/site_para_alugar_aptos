import requests
from django.core.management.base import BaseCommand
from icalendar import Calendar

from apartamento.models import Apartamento, Indisponibilidade


class Command(BaseCommand):
    help = "Busca as datas ocupadas no Airbnb e salva no site"

    def handle(self, *args, **options):
        apartamentos = Apartamento.objects.exclude(ical_url="")

        for apto in apartamentos:
            self.stdout.write(f"Sincronizando: {apto.nome}")
            try:
                response = requests.get(apto.ical_url)
                cal = Calendar.from_ical(response.content)

                apto.bloqueios.all().delete()

                for evento in cal.walk("VEVENT"):
                    inicio = evento.get("DTSTART").dt
                    fim = evento.get("DTEND").dt

                    Indisponibilidade.objects.create(
                        apartamento=apto, data_inicio=inicio, data_fim=fim
                    )

                self.stdout.write(self.style.SUCCESS("Sincronia concluida!"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Erro: {e}"))
