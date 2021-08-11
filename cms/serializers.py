from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import *
from rest_framework import serializers
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings


class RegistroUsuarioSerializer(serializers.ModelSerializer):
    # forma 1 para modificar algun atributo del model
    # password = serializers.CharField(write_only=True)

    def save(self):
        usuarioNombre = self.validated_data.get('usuarioNombre')
        usuarioApellido = self.validated_data.get('usuarioApellido')
        usuarioCorreo = self.validated_data.get('usuarioCorreo')
        usuarioTipo = self.validated_data.get('usuarioTipo')
        usuarioTelefono = self.validated_data.get('usuarioTelefono')
        password = self.validated_data.get('password')
        nuevoUsuario = UsuarioModel(
            usuarioNombre=usuarioNombre,
            usuarioCorreo=usuarioCorreo,
            usuarioApellido=usuarioApellido,
            usuarioTipo=usuarioTipo,
            usuarioTelefono=usuarioTelefono
        )
        nuevoUsuario.set_password(password)
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = UsuarioModel
        # fields = ['usuarioNombre', 'usuarioApellido']
        exclude = ['groups', 'user_permissions']
        # es para dar configuracion adicional a los atributos de un model serializer, usando el atributo extra_kwargs se puede editar la configuracion de si solo escritura, solo lectura, required, allow null, default y error messages
        # no es necesario volver a declarar las mismas configuraciones iniciales ()
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'usuarioId': {
                'read_only': True
            }
        }
class CustomPayloadSerializer(TokenObtainPairSerializer):
    # un funcion incorparada en python que devuelve un metodo de la clase de la cual se esta heredando
    # el metodo recibira la clase como primer argumento, cuando se llama a este metodo, se pasa a la clase como primer argumento en lugar de la instancia de la clase esto significa que puede utilizar la clase entera junto con sus propiedades dentro de este metodo sin tener que instanciar la clase
    @classmethod
    def get_token(cls, user: UsuarioModel):
        token = super(CustomPayloadSerializer, cls).get_token(user)
        print(token)
        token['usuarioTipo'] = user.usuarioTipo
        token['user_mail'] = user.usuarioCorreo
        token['mensaje'] = 'Holis'
        return token
class RegistroEventoSerializer(serializers.ModelSerializer):
    def save(self):
        fechaEvento = self.validated_data.get('fechaEvento')
        eventoTipo = self.validated_data.get('eventoTipo')
        eventoLugar = self.validated_data.get('eventoLugar')
        nuevoEvento = EventoModel(
            fechaEvento=fechaEvento,
            eventoTipo=eventoTipo,
            eventoLugar=eventoLugar
        )
        nuevoEvento.save()
        return nuevoEvento
    
    class Meta:
        model = EventoModel
        
class EventoSerializer(serializers.Serializer):
    class Meta:
        model = EventoModel
        fields = '__all__'