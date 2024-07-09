from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string


# Importing the required modules
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# Generate a pdf file
def download_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()
    # Create Canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    # Add some lines of text
    contents = [
        "Welcome the session",
        "Hope you are enjoying it"
    ]

    # loop throw the content
    for content in contents:
        textobj.textLine(content)

    # generate a pf file
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename="My_Pdf")






# Create your views here.
#def home_page(request):
 #   response_data = '''
  #      <ul>
   #         <li><a href= '/challenges/january'>January</a></li>
    #        <li><a href= '/challenges/february'>February</a></li>
     #       <li><a href= '/challenges/march'>March</a></li>
      #  </ul>
    #'''
    #return HttpResponse(response_data)

def home_page(request):
    months = ["january", "february", "march"]

    return render(request, "challenges/homepage.html", {
        "months": months
    })

'''
def monthly_challenge(request,month):
    # create a variable to store text, so that it can be updated with if else condition.
    challenge_text = None
    if month == "january":
        challenge_text = "Take a chill pill"
    #elif month == "Jan" or "jan":
        #return HttpResponseRedirect("/challenges/" + "january")
    elif month == "february":
        challenge_text = "pass internals"
    elif month == "march":
        challenge_text = "complete DBMS project"
    else:
        return HttpResponseNotFound("We are sorry, the month you entered is invalid!!!!")

    return HttpResponse(challenge_text)
'''

def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Take a chill pill"
    elif month == "february":
        challenge_text = "pass internals"
    elif month == "march":
        challenge_text = None
    else:
        return HttpResponseNotFound("We are sorry, the month you entered is invalid!!!!")

    return render(request, "challenges/challenge.html", {
        "month": month,
        "text": challenge_text,
    })



