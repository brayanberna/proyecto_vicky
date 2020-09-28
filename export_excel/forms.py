from django import forms

from django.contrib.auth.models import User
#birthdate = forms.DateField()
class RegisterForm(forms.Form):
  username = forms.CharField(required=True,
                              min_length=4, max_length=50,
                              widget=forms.TextInput(attrs={
                                'class': 'form-control',
                                'id': 'username',
                                'placeholder': 'Username'
                              }))
  email = forms.EmailField(required=True,
                              widget=forms.EmailInput(attrs={
                                'class': 'form-control',
                                'id': 'email',
                                'placeholder': 'example@codigofacilito.com'
                              }))
  password = forms.CharField(required=True,
                              widget=forms.PasswordInput(attrs={
                                'class': 'form-control',
                                'id': 'password',
                                'placeholder': 'Password'                                 
                              }))
  password2 = forms.CharField(label='Confirmar password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                  'class': 'form-control'
                                }))
  def clean_username(self):
    username = self.cleaned_data.get('username')

    if User.objects.filter(username=username).exists():
      raise forms.ValidationError('El username ya se encuentra en uso')
    return username

  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('El email ya se encuentra en uso')
    return email

  def clean(self):
    cleaned_data = super().clean()
    if cleaned_data.get('password2') != cleaned_data.get('password'):
      self.add_error('password2', 'El password no coincide')
  
  def save(self):
    return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password'),
          )

class RegisterFormIndex(forms.Form):
  localidad = forms.CharField(required=True,
                              widget=forms.Select(attrs={
                                'class': 'form-select',
                                'id': 'localidad',
                                'placeholder': 'localidad'
                              },
                              choices=(('ARIQUILDA', 'Ariquilda'), ('AROMA', 'Aroma'), ('HUARA', 'Huara'), ('PACHICA', 'Pachica'),
                                       ('PISAGUA', 'Pisagua'), ('BAJO SOGA', 'Bajo Soga'), ('TARAPACA', 'Tarapaca'), ('CHIAPA', 'Chiapa'),
                                       ('SIBAYA', 'Sibaya'))
                              ))
  nombre = forms.CharField(required=True,
                           min_length=4, max_length=50,
                           widget=forms.TextInput(attrs={
                            'class': 'form-control',
                            'id': 'nombre',
                            'placeholder': ''
                           }))
  rut = forms.CharField(label='RUT',
                        required=True,
                        widget=forms.TextInput(attrs={
                          'class': 'form-control',
                          'id': 'rut',
                          'name': 'rut',
                          'placeholder': 'Ingrese RUT',
                          'maxlength': '12',
                          'onblur': 'javascript:formatoRut(this.value,this.id)'
                        }))
  tipo_atencion = forms.CharField(label='Tipo de Atención',
                                  required=True,
                                  widget=forms.Select(attrs={
                                    'class': 'form-select',
                                    'id': 'tipo_atencion',
                                    'placeholder': 'tipo_atencion'
                                  },
                                  choices=(('CNS', 'CNS'), ('PCR', 'PCR'), ('RESCATE PACIENTES EN DOMICILIO', 'Rescate Pacientes en Domicilio'),
                                  ('RESCATE PACIENTE TELEFONICO', 'Rescate Paciente Telefónico'), ('CURACIONES', 'Curaciones'),
                                  ('SEGUIMIENTO COVID-19', 'Seguimiento COVID-19'))
                                  ))
  nacionalidad = forms.CharField(required=True,
                                label='Nacionalidad',
                                widget=forms.Select(attrs={
                                  'class': 'form-select',
                                  'id': 'nacionalidad',
                                  'placeholder': ''
                                },
                                choices=(('CHILENA', 'Chilena'), ('BOLIVIANA', 'Boliviana'), ('PERUANA', 'Peruana'),
                                ('ARGENTINA', 'Argentina'), ('COLOMBIANA', 'Colombiana'), ('VENEZOLANA', 'Venezolana'),
                                ('ECUATORIANA', 'Ecuatoriana'), ('PARAGUAYA', 'Paraguaya'), ('BRASILEÑA', 'Brasileña'))
                                ))
  etnia = forms.CharField(label='Etnia',
                          required=True,
                          widget=forms.Select(attrs={
                            'class': 'form-select',
                            'id': 'etnia',
                          },
                          choices=(('', 'Seleccionar'), ('AYMARA', 'Aymara'), ('QUECHUA', 'Quechua'), ('MAPUCHE', 'Mapuche'), ('DIAGUITA', 'Diaguita'),
                                    ('ATACAMEÑO', 'Atacameño'), ('KOLLA', 'Kolla'), ('RAPANUI', 'Rapanui'), ('KAWÉSQAR', 'Kawésqar'),
                                    ('YAGÁN', 'Yagán'))
                          ))
  sexo = forms.CharField(label='Sexo',
                         required=True,
                         widget=forms.Select(attrs={
                          'class': 'form-select',
                          'id': 'sexo',
                         },
                         choices=(('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino'))
                         ))
  rango_etario = forms.CharField(label='Rango Etario',
                        required=True,
                        widget=forms.Select(attrs={
                        'class': 'form-select',
                        'id': 'rango_etario',
                        },
                        choices=(('MENOR DE 1 MES', 'Menor de 1 mes'), ('1 MES', '1 Mes'), ('2 MESES', '2 Meses'), ('3 MESES', '3 Meses'),
                        ('4 MESES', '4 Meses'), ('5 MESES', '5 Meses'), ('6 MESES', '6 Meses'), ('7 A 11 MESES', '7 A 11 Meses'), 
                        ('12 A 17 MESES', '12 A 17 Meses'), ('18 A 23 MESES', '18 A 23 Meses'), ('24 A 47 MESES', '24 A 47 Meses'), 
                        ('48 A 59 MESES', '48 A 59 Meses'), ('60 A 71 MESES', '60 A 71 Meses'), ('6 - 9', '6 - 9 Años'), ('10 - 14', '10 - 14 Años'), 
                        ('15 - 19', '15 - 19 Años'), ('20 - 24', '20 - 24 Años'), ('25 - 29', '25 - 29 Años'), ('30 - 34', '30 - 34 Años'),
                        ('35 - 39', '35 - 39 Años'), ('40 - 44', '40 - 44 Años'), ('45 - 49', '45 - 49 Años'), ('50 - 54', '50 - 54 Años'),
                        ('55 - 59', '55 - 59 Años'), ('60 - 64', '60 - 64 Años'), ('65 - 69', '65 - 69 Años'), ('70 - 74', '70 - 74 Años'),
                        ('75 - 79', '75 - 79 Años'), ('80 Y MAS', '80 y más'))
                        ))
  edad = forms.CharField(label='Edad',
                      required=True,
                      widget=forms.TextInput(attrs={
                        'class': 'form-control',
                        'id': 'edad',
                        'name': 'edad',
                        'placeholder': '',
                      }))