from django.urls import path, include
from . import views
#from Iple.Apps.GestionAcademica.views import Indice

urlpatterns = [
    path('',views.Indice, name='Indice'),
# Para poder acceder a esta clase debemos hacer la creación de la url correspondiente en el archivo urls.py:

#	path(r'^reporte_personas_pdf/$',login_required(ReportePersonasPDF.as_view()), name="reporte_personas_pdf"),

# url(r'^$',views.index, name='Index')
 ]