from csv import excel

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, FormView, ListView, DetailView
import code128
import os



from .models import BarCodeModel
from .forms import BarCodeModelForm, UploadFileForm
from django.core.files import File



class BarCodeCreateView(CreateView):
    template_name = 'bar_code_generated.html'
    model = BarCodeModel
    success_url = reverse_lazy('bar_codes:list')
    form_class = BarCodeModelForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        name_bar_code_extension = str(self.object.code)+".png"
        img = code128.image(self.object.code)
        f = open(name_bar_code_extension, "wb")
        img.save(name_bar_code_extension)
        f.close()
        reopen = open(name_bar_code_extension, "rb")
        django_file = File(reopen)
        self.object.bar_code.save(name_bar_code_extension, django_file, save=True)
        reopen.close()
        self.object.save()
        os.remove(name_bar_code_extension)

        return super(BarCodeCreateView, self).form_valid(form)


class BarCodeListView(ListView):
    template_name = 'bar_code_list.html'
    model = BarCodeModel
    paginate_by = 5


class BarCodeDetailView(DetailView):
    template_name = 'bar_code_detail.html'
    model = BarCodeModel
    queryset = BarCodeModel.objects.all()


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv", file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'bar_code_upload.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


