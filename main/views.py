from django.shortcuts import render

def home(request):
    result = None
    if request.method == "POST":
        # 1. Get names
        a = request.POST.get('n1', '').lower().replace(' ', '')
        b = request.POST.get('n2', '').lower().replace(' ', '')
        
        # 2. FLAMES character cancellation logic
        for char in a[:]:
            if char in b:
                a = a.replace(char, '', 1)
                b = b.replace(char, '', 1)
        
        count = len(a + b)
        
        # 3. The FLAMES elimination logic
        flames = ['Friends', 'Lovers', 'Attraction', 'Marriage', 'Enemy', 'Sibling']
        
        if count > 0:
            while len(flames) > 1:
                index = (count % len(flames)) - 1
                if index >= 0:
                    right = flames[index + 1:]
                    left = flames[:index]
                    flames = right + left
                else:
                    flames.pop()
            result = flames[0]
        else:
            result = "Soulmates" # Case for identical names

    return render(request, 'index.html', {'result': result})