from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Camera
from .forms import Camera, CameraForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView


# def camera_list(request):
#     cameras = Camera.objects.all().order_by('-id')
#     return render(request, 'camera_list.html', {'cameras': cameras})
class CameraList(ListView):
    model = Camera
    template_name = 'camera_list.html'
    context_object_name = 'cameras'

# def camera_detail(request, pk):
#     camera = Camera.objects.get(id=pk)
#     return render(request, 'camera_detail.html', {'camera':camera})

class CameraDetail(DetailView):
    model = Camera
    template_name = 'camera_detail.html'
    context_object_name = 'camera'


# def create_camera(request):
#     if request.method == 'POST':
#         form = CameraForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('camera')
#     else:
#         form = CameraForm()
#     return render(request, 'create_camera.html', {'form': form})

class CameraCreate(CreateView):
    model = Camera
    form_class = CameraForm
    template_name = 'create_camera.html'
    success_url = reverse_lazy('camera')

# def update_camera(request, pk):
#     camera = Camera.objects.get(id=pk)
#     if request.method == 'POST':
#         camera.brand = request.POST['brand']
#         camera.price = request.POST['price']
#         image = request.FILES.get('image')
#         if image:
#             camera.image = image
#         camera.save()
#         return redirect('camera-detail', pk=pk)
#     return render(request, 'update_camera.html', {'camera': camera})

# def update_camera(request, pk):
#     camera = get_object_or_404(Camera, id=pk)
#     form = CameraForm(request.POST, request.FILES, instance=camera)
#     if form.is_valid():
#         form.save()
#         return redirect('camera-detail', camera.id)
#     else:
#         form = CameraForm(instance=camera)
#     return render(request, 'update_camera.html', {'form':form})

class CameraUpdate(UpdateView):
    model = Camera
    form_class = CameraForm
    template_name = 'update_camera.html'
    success_url = reverse_lazy('camera')

# def delete_camera(request, pk):
#     camera = Camera.objects.get(id=pk)
#     if request.method == 'POST':
#         camera.delete()
#         return redirect('camera')
#     return render(request, 'delete_confirm.html', {'camera': camera})



class CameraDelete(DeleteView):
    model = Camera
    template_name = 'camera_confirm_delete.html'
    success_url = reverse_lazy('camera')