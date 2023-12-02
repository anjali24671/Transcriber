from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import transcriptForm

# Create your views here.
class homeView(FormView):
    template_name = 'home.html'
    form_class = transcriptForm
    success_url = 'answer/' 

    def form_valid(self, form):
        url = form.cleaned_data['URL']
        lang = form.cleaned_data['lang']
        print(lang)
        from base import getContent
        transcript = getContent(url, lang)
        if transcript[:11]=='Bad Request':  
            return render(self.request, 'home.html', {'form':form,'transcript': transcript})
        return render(self.request, 'answer.html', {'transcript': transcript})

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class ansView(TemplateView):
    template_name = 'answer.html'
    
