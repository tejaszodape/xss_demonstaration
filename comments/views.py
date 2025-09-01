# views.py
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .models import StoredComment

def xss_demo(request):
    xss_type = "safe"
    output = StoredComment.objects.all()
    result = ""
    last_payload = ""  # For DOM-based demo

    if request.method == "POST":
        payload = request.POST.get("payload", "")
        xss_type = request.POST.get("xss_type", "safe")

        # Handle clear
        if request.POST.get("action") == "clear":
            StoredComment.objects.all().delete()
            return HttpResponseRedirect(request.path)

        # Handle Persistent
        if xss_type == "persistent":
            if payload:
                StoredComment.objects.create(text=payload)
            return HttpResponseRedirect('?xss_type=persistent')

        # Handle Reflected, DOM, Safe
        else:
            # Store in messages for one-time display
            messages.add_message(request, messages.INFO, payload)
            # Redirect and preserve xss_type
            return HttpResponseRedirect(f'?xss_type={xss_type}&payload={payload}')

    # Read from URL after redirect
    if request.GET.get("xss_type") in ["persistent", "reflected", "dom", "safe"]:
        xss_type = request.GET.get("xss_type")

    # Get one-time message (cleared after read)
    if messages.get_messages(request):
        for message in messages.get_messages(request):
            result = str(message)

    # Always get payload from URL for DOM demo
    last_payload = request.GET.get("payload", "")

    return render(request, "xss_demo.html", {
        "result": result,
        "xss_type": xss_type,
        "output": output,
        "payload": last_payload,  # Pass to template so input shows it
    })