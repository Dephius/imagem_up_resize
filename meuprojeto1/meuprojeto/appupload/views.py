from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
from meuprojeto.appupload.form import ImagemForm
from meuprojeto.appupload.models import FileUp




def galeria(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = FileUp(img=request.FILES['img'])
            newimg.save()

        return HttpResponseRedirect(reverse('galeria'))
    else:
        form = ImagemForm()

    imagens = FileUp.objects.all()

    return render(
        request,
        'lista.html',
        {'imagens': imagens, 'form': form}
    )