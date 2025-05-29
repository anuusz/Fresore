from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib import colors
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

def generate_invoice_pdf(order):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    
    # Header
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 750, "INVOICE")
    p.setFont("Helvetica", 12)
    p.drawString(100, 730, f"Invoice #: {order.invoice_number}")
    p.drawString(100, 710, f"Date: {order.created.strftime('%B %d, %Y')}")
    
    # Customer Info
    p.drawString(100, 680, f"Customer: {order.user.get_full_name() or order.user.username}")
    p.drawString(100, 660, "Billing Address:")
    p.drawString(120, 640, order.billing_address)
    
    # Items Table
    data = [['Item', 'Price', 'Qty', 'Total']]
    for item in order.items.all():
        data.append([
            item.product.name,
            f"${item.price:.2f}",
            item.quantity,
            f"${item.get_cost():.2f}"
        ])
    
    # Add total row
    data.append(['', '', 'Total:', f"${order.total:.2f}"])
    
    table = Table(data, colWidths=[300, 80, 80, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -2), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    table.wrapOn(p, 100, 600)
    table.drawOn(p, 100, 400)
    
    # Footer
    p.setFont("Helvetica", 10)
    p.drawString(100, 100, "Thank you for your business!")
    p.drawString(100, 80, "Please make payment within 14 days.")
    
    p.showPage()
    p.save()
    
    buffer.seek(0)
    return buffer

def send_invoice_email(order):
    subject = f"Your Invoice #{order.invoice_number}"
    message = render_to_string('shop/email_invoice.html', {
        'order': order,
    })
    
    email = EmailMessage(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [order.user.email],
    )
    
    # Attach PDF
    pdf_buffer = generate_invoice_pdf(order)
    email.attach(
        f'invoice_{order.invoice_number}.pdf',
        pdf_buffer.getvalue(),
        'application/pdf'
    )
    
    email.send()