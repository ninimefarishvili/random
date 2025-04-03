from ninja import Router

router = Router()

@router.get("/secret")
def secret(request):
    return {"message": "This is a secret message"}

auth_router = Router()

