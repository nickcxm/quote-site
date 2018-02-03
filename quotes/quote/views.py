from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView
from .models import Tag,Quote
from django.db.models import Q
from .forms import QuoteForm
# Create your views here.
class IndexView(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quote_list'
    def get_context_data(self, **kwargs):
        context=super(IndexView,self).get_context_data(**kwargs)
        form=QuoteForm()
        quote_list=Quote.objects.all()
        context.update({
            'form':form,
            'quote_list':quote_list
        })
        return context
    paginate_by = 1
class TagView(ListView):
    model = Quote
    template_name = 'index.html'
    context_object_name = 'quote_list'
    def get_context_data(self, **kwargs):
        context=super(TagView,self).get_context_data(**kwargs)
        tag=get_object_or_404(Tag,pk=self.kwargs.get('pk'))
        form=QuoteForm()
        quote_list=Quote.objects.all().filter(tags=tag)
        context.update({
            'form':form,
            'quote_list':quote_list
        })
        return context

def add(request):
    if request.method=="POST":
        form=QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            quote_list=Quote.objects.all()
            context={'form':form,
                     'quote_list':quote_list
                     }
            return render(request,'index.html',context=context)
    return redirect('/')

def search(request):
    q=request.GET.get('q')
    error_msg=''
    form=QuoteForm()
    if not q:
        error_msg="input some words!"
        return render(request,'index.html',{'error_msg':error_msg})
    quote_list=Quote.objects.filter(Q(text__icontains=q))
    return render(request,'index.html',{'error_msg':error_msg,
                                        'form':form,
                                        'quote_list':quote_list
                                        })