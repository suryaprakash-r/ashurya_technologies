from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.http import JsonResponse

from .models import Contact


def contact_view(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        service = request.POST.get("service")
        message = request.POST.get("message")

        # Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            message=message
        )
        
        
        admin_subject = f"New Lead: {name} - {service}"

        admin_html = f"""
        <html>
        <body style="font-family:Arial;background:#f6f8fb;padding:20px;">
        <div style="max-width:600px;margin:auto;background:#fff;padding:25px;border-radius:10px;border:1px solid #e5e7eb;">

            <h2 style="color:#2563eb;">New Contact Lead</h2>
            <hr>

            <p><b>Name:</b> {name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Phone:</b> {phone}</p>
            <p><b>Service:</b> {service}</p>

            <hr>

            <p><b>Message:</b></p>
            <p>{message}</p>

            <hr>
            <p style="font-size:12px;color:#6b7280;">
                Ashurya Technologies Lead System
            </p>

        </div>
        </body>
        </html>
        """

        admin_email = EmailMultiAlternatives(
            admin_subject,
            "New lead received",
            settings.EMAIL_HOST_USER,
            ["r.suryaprakash0800@gmail.com"]
        )

        admin_email.attach_alternative(admin_html, "text/html")
        admin_email.send()
        
        user_subject = "We received your message - Ashurya Technologies"

        user_html = f"""
        <html>
        <body style="font-family:Arial;background:#f6f8fb;padding:20px;">
        <div style="max-width:600px;margin:auto;background:#fff;padding:25px;border-radius:10px;border:1px solid #e5e7eb;">

            <h2 style="color:#2563eb;">Hi {name},</h2>

            <p>Thank you for contacting <b>Ashurya Technologies</b>.</p>

            <p>We have received your request regarding <b>{service}</b>.</p>

            <p>Our team will get back to you within <b>24 hours</b>.</p>

            <hr>

            <p style="font-size:12px;color:#6b7280;">
                Ashurya Technologies Team
            </p>

        </div>
        </body>
        </html>
        """

        user_email = EmailMultiAlternatives(
            user_subject,
            "We received your message",
            settings.EMAIL_HOST_USER,
            [email]
        )

        user_email.attach_alternative(user_html, "text/html")
        user_email.send()

        # ==============================
        # ⚡ AJAX RESPONSE
        # ==============================
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({"status": "success"})

        # fallback
        return redirect("contact_success")

    return render(request, "contact/contact.html")