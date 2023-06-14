from django.shortcuts import render

def convert_units(request):
    if request.method == 'POST':
        # Odczytaj wartości przesłane przez formularz
        value = float(request.POST.get('value'))
        from_unit = request.POST.get('from_unit')
        to_unit = request.POST.get('to_unit')

        # Wykonaj przeliczenie jednostek
        result = convert(value, from_unit, to_unit)

        # Prześlij wynik do szablonu
        return render(request, 'converter/convert_units.html', {'result': result})

    # Jeśli metoda żądania jest GET, wyświetl pusty formularz
    return render(request, 'converter/convert_units.html')


def convert(value, from_unit, to_unit):
    # Logika przeliczania jednostek
    # Implementuj odpowiednie wzory przeliczeniowe dla każdej jednostki
    if from_unit == 'cm3' and to_unit == 'dm3':
        result = value / 1000
    elif from_unit == 'dm3' and to_unit == 'cm3':
        result = value * 1000
    elif from_unit == 'µl' and to_unit == 'ml':
        result = value / 1000
    elif from_unit == 'ml' and to_unit == 'µl':
        result = value * 1000
    elif from_unit == 'ml' and to_unit == 'l':
        result = value / 1000
    elif from_unit == 'l' and to_unit == 'ml':
        result = value * 1000
    elif from_unit == 'g' and to_unit == 'µg':
        result = value * 1000000
    elif from_unit == 'g' and to_unit == 'mg':
        result = value * 1000
    elif from_unit == 'g' and to_unit == 'ng':
        result = value * 1000000000
    # Dodaj inne przypadki przeliczeń jednostek

    return result

# Create your views here.
