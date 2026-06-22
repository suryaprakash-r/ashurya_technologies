import logging

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import Contact

logger = logging.getLogger(__name__)

@csrf_exempt
def contact_view(request):

    if request.method == "POST":

        try:

            name = request.POST.get(
                "name", ""
            ).strip()

            company_name = request.POST.get(
                "company_name", ""
            ).strip()

            email = request.POST.get(
                "email", ""
            ).strip()

            phone = request.POST.get(
                "phone", ""
            ).strip()

            service = request.POST.get(
                "service", ""
            ).strip()

            message = request.POST.get(
                "message", ""
            ).strip()

            lead = Contact.objects.create(
                name=name,
                company_name=company_name,
                email=email,
                phone=phone,
                service=service,
                message=message
            )

            admin_subject = (
                f"New Lead: {name} - {service}"
            )

            admin_html = f"""
            <h2>New Contact Lead</h2>

            <p><b>Name:</b> {name}</p>
            <p><b>Company:</b> {company_name}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Phone:</b> {phone}</p>
            <p><b>Service:</b> {service}</p>

            <hr>

            <p>{message}</p>
            """

            admin_email = EmailMultiAlternatives(
                admin_subject,
                "New lead received",
                settings.EMAIL_HOST_USER,
                ["r.suryaprakash0800@gmail.com"]
            )

            admin_email.attach_alternative(
                admin_html,
                "text/html"
            )

            admin_email.send()

            user_subject = (
                "We received your message - Ashurya Technologies"
            )

            user_html = f"""
            <h2>Hi {name},</h2>

            <p>
            Thank you for contacting
            Ashurya Technologies.
            </p>

            <p>
            Our team will review your
            request and get back to you
            within 24 hours.
            </p>

            <p>
            Regards,<br>
            Ashurya Technologies
            </p>
            """

            user_email = EmailMultiAlternatives(
                user_subject,
                "We received your message",
                settings.EMAIL_HOST_USER,
                [email]
            )

            user_email.attach_alternative(
                user_html,
                "text/html"
            )

            user_email.send()

            if request.headers.get(
                "X-Requested-With"
            ) == "XMLHttpRequest":

                return JsonResponse({
                    "status": "success"
                })

            return redirect(
                "contact_success"
            )

        except Exception as e:

            logger.error(str(e))

            if request.headers.get(
                "X-Requested-With"
            ) == "XMLHttpRequest":

                return JsonResponse(
                    {
                        "status": "error",
                        "message": str(e)
                    },
                    status=500
                )

            return render(
                request,
                "contact/contact.html",
                {
                    "error":
                    "Something went wrong."
                }
            )

    return render(
        request,
        "contact/contact.html"
    )