hotelList = ["Bankhele Snacks","Shivnandini Idli", "Shubham Davangiri Dosa", "Gadkari Vadapav","Hotel Mayur","Yevale Amrutulya","Saiba Amrutulya","Indrajeet Chinese","Ratan Sweets","Santa's Roll Corner","Café Crème","Moraya Khaugalli","Hotel Ravikiran","Hotel Vishakha","Hotel Visawa","Hotel New Umbar","Hotel Samadhan","Hotel Celebration","Dattakrupa Pav Bhaji","Hotel Dinesh","Hotel Swagat","Hotel Shivsagar","Hotel Athavan","Chand Biryani","Sher-e-Punjab","Bholenath Ice-Cream","Bharkhadevi Ice-Cream","Kekiz","Poona Bakery","Amar Bakery","Ribbons & Balloons","Maitri Cake","Monginis"]

f = open("draft.html","r")
html = f.read()
f.close()

for hotel in hotelList:
    f = open(hotel.replace(" ","")+".html","w+")
    f.truncate()
    f.write(html)
    f.close
