from django.contrib import admin
from .models import Vibe
from .models import Genero
from .models import Musica
from .models import Watcher
from .models import Player

admin.site.register(Vibe)
admin.site.register(Genero)
admin.site.register(Musica)
admin.site.register(Watcher)
admin.site.register(Player)

# Register your models here.
