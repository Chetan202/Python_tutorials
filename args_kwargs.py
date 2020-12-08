def funargs(normal,*argsname,**kwargsroll):
    print(normal)
    for i in argsname:
        print(i)
    for key,value in kwargsroll.items():
        print(f"{key} value is: {value}")

args=["Chetan","Dipesh","Brijesh","Rish"]
kwargs={"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
nmal="Hii I am Chetan"    
funargs(nmal,*args,**kwargs)     