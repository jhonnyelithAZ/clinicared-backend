from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/simulate",
    tags=["External Simulators"]
)

class AdmissionCheckRequest(BaseModel):
    national_id: str

class MessageNotificationRequest(BaseModel):
    recipient: str
    message: str
    channel: str = "SMS"  # SMS o EMAIL

@router.post("/admissions/verify")
def simulate_admission_check(payload: AdmissionCheckRequest):
    """Simula la validación de estado o afiliación en el sistema de admisiones externo."""
    is_active = int(payload.national_id[-1]) % 2 == 0 if payload.national_id.isdigit() else True
    return {
        "national_id": payload.national_id,
        "status": "ACTIVE" if is_active else "PENDING_AUTHORIZATION",
        "network": "ClínicaRed Preferred",
        "message": "Verificación de admisiones simulada con éxito."
    }

@router.post("/messaging/send")
def simulate_send_message(payload: MessageNotificationRequest):
    """Simula el envío de un mensaje o recordatorio de cita (SMS/Email)."""
    return {
        "status": "SENT",
        "channel": payload.channel.upper(),
        "recipient": payload.recipient,
        "simulated_gateway_response": "OK_200_DISPATCHED"
    }