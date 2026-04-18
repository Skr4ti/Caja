from django.shortcuts import render
from django.utils import timezone
from .models import Sale
from django.shortcuts import redirect, get_object_or_404

def caja(request):

    if request.method == "POST":
        name = request.POST["name"]
        price = int(request.POST["price"])
        amount = int(request.POST["amount"])
        payment = int(request.POST["payment"])

        total = price * amount

        if payment < total:
            sales = Sale.objects.all().order_by("-time")
            return render(request, "caja.html", {
                "sales": sales,
                "error": "Pago insuficiente"
            })
            Sale.objects.create(
            name=name,
            price=price,
            amount=amount,
            payment=payment
    )

  

    fecha = request.GET.get("fecha")

    if fecha:
        sales = Sale.objects.filter(time__date=fecha).order_by("-time")
    else:
        hoy = timezone.now().date()
        sales = Sale.objects.filter(time__date=hoy).order_by("-time")

    # totales
    total_vendido = sum(s.total() for s in sales)
    total_recibido = sum(s.payment for s in sales)
    total_vuelto = sum(s.change() for s in sales)

    efectivo_caja = total_recibido - total_vuelto

    cantidad_ventas = sales.count()

    return render(request, "caja.html", {
        "sales": sales,
        "total_caja": total_vendido,
        "total_vendido": total_vendido,
        "total_recibido": total_recibido,
        "total_vuelto": total_vuelto,
        "efectivo_caja": efectivo_caja,
        "cantidad_ventas": cantidad_ventas,
        "fecha": fecha
    })

def borrar_venta(request, id):
    sale = get_object_or_404(Sale, id=id)
    sale.delete()
    return redirect('caja')

def editar_venta(request, id):
    sale = get_object_or_404(Sale, id=id)

    if request.method == "POST":
        sale.name = request.POST["name"]
        sale.price = int(request.POST["price"])
        sale.amount = int(request.POST["amount"])
        sale.payment = int(request.POST["payment"])
        sale.save()

        return redirect('caja')

    return render(request, "editar.html", {"sale": sale})