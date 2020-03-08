from django.shortcuts import render, redirect, get_object_or_404
from .models import List
from .forms import ListForm
from django.contrib import messages
# these are the python methods for our program

#home will show the to-do list
def home(request):
    #if there is a post show it 
    if request.method == 'POST':
        #in the form of a "ListForm" our custom class from djangos List 
        form = ListForm(request.POST or None)
        #if the item in the list is a valid item, which will be when it has not been deleted
        if form.is_valid():
            #save it
            form.save()
            #show all of the items on the to-do list 
            all_items = List.objects.all
            #show a message that an item has been added to the to-do list
            messages.success(request, ('Item Has Been Added To List!'))
            #render the request ie. show the home page again and show all of the items in the list which will be updated after save() is called
        return render(request, "home.html", {'all_items': all_items})
    #if a new item is not added, just show all the items that are already there
    else:
        all_items = List.objects.all 
        return render(request, "home.html", {'all_items': all_items})
#deleting an object by its list_id, using get_object_or_404 which will throw an error if the object is not found. This method..
#is useful when running the server non-stop and avoiding errors from that 
def delete(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    #call List's delete() method
    item.delete()
    #show a message that the item has been deleted
    messages.success(request, ('Item Has Been Deleted'))
    #return to the home page
    return redirect('home')
#cross off an item from the list, this will change the Boolean value of completed which tells our html code to show it as darkened...
#showing the user their item has been completed, save it and return to home 
def cross_off(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.completed=True
    item.save()
    return redirect('home')
#uncross, this will make the item in the to-do list shown as not being completed, then return to home 
def uncross(request, list_id):
    item = get_object_or_404(List, pk=list_id)
    item.completed=False
    item.save()
    return redirect('home')
# edit will get the item by id and bring a post up for the user to enter their edits into
def edit(request, list_id):
    if request.method == 'POST':
        item = get_object_or_404(List, pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            #save it
            form.save()
            #show a message 
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        #otherwise just go back without editing 
        item = get_object_or_404(List, pk=list_id)
        return render(request, 'edit.html', {'item':item})
