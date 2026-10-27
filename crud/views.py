from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm, ImageSizeLimitationForm
from django.http import HttpResponseRedirect


class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create'


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods
    template_name = 'crud/goods_detail.html'


class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = '/crud/goods_list'


class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'


class GoodsCreateWithImageSizeLimitation(generic.CreateView):
    form_class = ImageSizeLimitationForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_list'


class CustomDeleteView(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'


def delete(self, request, *args, **kwargs):
    self.object = self.get_object()
    success_url = self.get_success_url()
    self.object.custom_delete()
    return HttpResponseRedirect(success_url)
