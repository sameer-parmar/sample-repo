from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import PlacementStories
from .forms import PlacementStoriesForm  # Make sure to import your form
from django.shortcuts import get_object_or_404      
def placement_stories(request):
    # Pagination setup
    placement_stories = PlacementStories.objects.all().order_by('-id')
    paginator = Paginator(placement_stories, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Form handling for superusers
    form = None
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PlacementStoriesForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('placement_stories')  # Redirect to clear POST data
        else:
            form = PlacementStoriesForm()

    return render(request, 'placement_stories.html', {
        'page_obj': page_obj,
        'form': form
    })
def story_detail(request, story_id):
    story = get_object_or_404(PlacementStories,id = story_id)

    return render(request, 'storydetail.html',{'story':story})