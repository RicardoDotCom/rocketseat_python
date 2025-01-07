import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # Criar o pagamento na instituição financeira
        bank_payment_id = str(uuid.uuid4())

        # qr code - é uma informação, podendo ser texto/número, que foi gerada uma imagem
        hash_payment = f'hash_payment_{bank_payment_id}'

        # criação da imagem biblioteca QR CODE PYTHON 
        img = qrcode.make(hash_payment)
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")

        return {"bank_payment_id":bank_payment_id,
                "qr_code_path": f"qr_code_payment_{bank_payment_id}"}
