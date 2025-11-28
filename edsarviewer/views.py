from django.http import JsonResponse
from django.shortcuts import render
import subprocess

#Defines the view function, Django will call this function when "edsar_viewer" had been accessed 
def edsarview(request):

    #Check if HTTP request 'GET' method was made
    if request.method == 'POST':

         #Run external python program
        result = subprocess.run(['python', 'edsarviewer/convert.py'],
        capture_output=True, text=True)

        return render(request, 'index.html', {
            'output': result.stdout,
            'error': result.stderr
        })

    #Sends JSON response back to the browser with message
    #return JsonResponse({'Message': 'Executed Successfully!'})
    return render(request, 'index.html')
