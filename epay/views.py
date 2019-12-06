from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse,JsonResponse,QueryDict
from .models import Item

# Create your views here.
def home(request):

    context = {
        'items' : Item.objects.all()
    }
    return render(request, 'epay/home.html', context)

def searchView(request):
    return render(request, 'epay/search.html')

    # return JsonResponse({
    #     'Items': list( Item.objects.values()),
    # })



def searchView1(request):
    return JsonResponse({
        'Items': list( Item.objects.values()),
    })


def signup(request):
    return render(request, 'epay/signup.html', {'title' : 'signup'})

class PostListView(ListView):
    model = Item
    template_name = 'epay/home.html'
    context_object_name ='items'
    ordering = ['-date_listed']

class PostDetailView(DetailView):
    model = Item

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Item
    fields = ['itemTitle','itemDescription','price','endTime', 'itemPicture']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Item
    fields = ['itemTitle','itemDescription','price','endTime']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Item
    success_url = '/'
    def test_func(self):
        item = self.get_object()
        if self.request.user == item.seller:
            return True
        return False


def bidView(request):

    user = request.user
    bid = request.POST.get('bid')
    item = request.POST.get('item')

    return JsonResponse({
        'Items': list( Item.objects.values()),
    })


    class bidview(LoginRequiredMixin,CreateView):
        model = Item
        fields = ['Biddings']

        def form_valid(self, form):
            form.instance.seller = self.request.user
            return super().form_valid(form)
