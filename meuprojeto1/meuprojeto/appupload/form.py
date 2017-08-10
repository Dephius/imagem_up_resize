# -*- coding: utf-8 -*-

from django import forms


class ImagemForm(forms.Form):
    img = forms.ImageField(
        label='Selecione a imagem'
    )