from django.http import HttpResponseRedirect


# Login Function

def login(username, password):
    username = ('username'),
    if [username] is True:
        print('Success!')
    elif [password] is False:
        print ('Invalid Password!')


# Redirect sucessfull function                               # If Login successful re-direct over to admin.py to run script

def redirect_view(request):
    redirect = HttpResponseRedirect('/redirect/success')
    redirect = ['location']
    redirect.status_code
    return HttpResponseRedirect('/redirect/successs')

    


# Redirect Invalid function                                  #  If unsucessful re-redirect over to "lost password page"