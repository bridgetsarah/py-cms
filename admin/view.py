from new_post import new_post
                                                                     # Totally needs a re-write.. Way to messy coding.
def post_upload(request):
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST())    

        if form.is_valid():
            content = form.cleaned_data['content']
            created_at = form.cleaned_data['created_at']
            post = m.post.objects.create(content=content,
                                        created_at=created_at)
            return HttpResponseRedirect(reverse('post_detail',
                                                kwargs={'post_id'}))
    return render(request, post 'post/post_upload.html', {
        'form': form,
        })                                                                        