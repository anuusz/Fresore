from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Category, Product, Order
from .serializers import (
    CategorySerializer, 
    ProductSerializer, 
    OrderSerializer
)
from django.shortcuts import get_object_or_404
from .utils import generate_invoice_pdf
from django.http import HttpResponse
from django.views.generic import View

class InvoicePDF(View):
    def get(self, request, pk):
        # Simple text response as example
        content = f"Invoice for Order #{pk}\nThank you for your purchase!"
        return HttpResponse(content, content_type='text/plain')

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        category_slug = self.request.query_params.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    lookup_field = 'slug'

class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderList(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderDetail(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
class InvoicePDF(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=kwargs['pk'], user=request.user)
        buffer = generate_invoice_pdf(order)
        
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="invoice_{order.invoice_number}.pdf"'
        return response