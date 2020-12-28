def custom_processors(request):
    return {
       "domain_with_protocol": request.build_absolute_uri('/')[:-1].strip("/")
    }