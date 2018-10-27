from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Recipe


class IndexView(generic.ListView):
    template_name = 'recipe/index.html'
    context_object_name = 'recipes'

    def get_queryset(self):
	    """
	    Return the last five published recipes (not including those set to be
	    published in the future).
	    """
	    return Recipe.objects.filter(
	        pub_date__lte=timezone.now()
	    ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'

    def get_queryset(self):
        """
        Excludes any recipes that aren't published yet.
        """
        return Recipe.objects.filter(pub_date__lte=timezone.now())


class EditView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/edit.html'


def create(request):
	return redirect(reverse('recipe:index'))

def send_to_cart(request, pk):
	return redirect(reverse('recipe:index'))


def delete(request, pk):
	recipe = get_object_or_404(Recipe, pk=pk)
	recipe.delete()
	return redirect(reverse('recipe:index'))


def vote(request):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
    return render(request, 'recipe/base.html')#, {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('recipe:results', args=(question.id,)))
