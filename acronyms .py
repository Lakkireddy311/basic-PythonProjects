input=input("enter a phrase:")
text=input.split()
short_form=""
for i in text:
    short_form=short_form+str(i[0]).upper()
print(short_form)