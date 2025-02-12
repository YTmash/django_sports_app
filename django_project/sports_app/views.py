from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
attractions = [ 
  { 'attraction_name' : 'Niagra Falls', 'prov' : 'Ontario'}, 
  { 'attraction_name' : 'West Edmonton Mall', 'prov' : 
'Alberta'}, 
  { 'attraction_name' : 'Stanley Park', 'prov' : 'British Columbia'}, 
  { 'attraction_name' : 'Heritage Park Historical Village', 
'prov' : 'Alberta'}, 
  { 'attraction_name' : 'Canadian Museum for Human Rights', 
'prov' : 'Manitoba'}, 
  { 'attraction_name' : 'Signal Hill', 'prov' : 'Newfoundland'}, 
  { 'attraction_name' : 'Old Quebec', 'prov' : 'Quebec'}, 
  { 'attraction_name' : 'Western Development Museum', 'prov' : 
'Saskatchewan'}, 
  { 'attraction_name' : 'Tidal Bore', 'prov' : 'New Brunswick'}, 
  { 'attraction_name' : 'Peggy\'s Cove', 'prov' : 'Nova Scotia'}, 
  { 'attraction_name' : 'Green Gables', 'prov' : 'Prince Edward Island'} 
] 
 
def home(request): 
    return render(request, 'sports_app/home.html') 

def about(request): 
    return render(request, 'sports_app/about.html') 

def contact(request): 
    return render(request, 'sports_app/contact.html') 



def sport_list(request):
    sports = ["Soccer", "Basketball", "Lacrosse"] 
    return render(request, 'sports_app/sport_list.html', {'sports': sports})
