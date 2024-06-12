from .predict import predict


# Create your views here.
def predictPage(request):
  if request.method == "POST" and request.POST.get("predictbtn", "") == "predictbtn":
    print("predict bisa")
    print(request.POST.get("predictbtn", ""))
    url = request.POST["url"]
    text = request.POST["text"]
    
    output = predict(url, text)
    return output
  
