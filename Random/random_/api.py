from ninja import Router, File, UploadedFile
from .models import Ragaca
from .serializers import RagacaSchema

router = Router()

@router.post("/ragaca/upload", response=RagacaSchema)
def create_ragaca(request, name: str, last_name: str, image: UploadedFile = File(...)):
    ragaca = Ragaca.objects.create(name=name, last_name=last_name, image=image)
    return {
        "id": ragaca.id,
        "name": ragaca.name,
        "last_name": ragaca.last_name,
        "image": request.build_absolute_uri(ragaca.image.url) if ragaca.image else None
    }

auth_router = Router()

